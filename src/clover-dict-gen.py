#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import jieba
import pypinyin
import opencc

import argparse
import os
import sys

# 从 pypinyin 库里得到所有文字及其若干个拼音
pinyin_dict = pypinyin.pinyin_dict.pinyin_dict
replace_symbol_to_no_symbol = pypinyin.style._utils.replace_symbol_to_no_symbol
initials_set = set(pypinyin.style._constants._INITIALS)   # 声母表
initials_set.add('ng')

# 修复一些多音字错误
pypinyin.load_phrases_dict({
    '还珠格格': [['huán'], ['zhū'], ['gé'], ['gé']]
    })



class DictGenerator:
    def fixPinyin(self, pinyin):
        """
            检查拼音，规范化拼音，失败则返回 None
                因为输入法里不允许出现单声母的拼音，
                    否则会出现无法输入正常的词组的情况。
                而汉字中比如 “嗯” 的拼音是 n 和 ng
                通常输入法会让 “嗯” 的拼音为 en
        """
        if pinyin in initials_set:
            if pinyin == 'n':
                pinyin = 'en'
            elif pinyin == 'm':
                pinyin = 'mu'
            elif pinyin == 'ng':
                pinyin = 'en'
            else:
                return None  # 不允许出现单声母的拼音
        return pinyin

    def __init__(self):
        """
            初始化函数，定义了字词频率所需的基本数据结构
            self.word_dict 和 self.phrase_r
        """

        """
            从 jieba 库里的 pinyin_dict 经过 replace_symbol_to_no_symbol 转换得到：
                self.word_pinyin_s 所有字的字音字典，格式为
                    {
                        unicode编码: [音1, 音2, ...],
                        unicode编码: [音1, 音2, ...],
                        unicode编码: [音1, 音2, ...],
                        ...
                    }
        """
        jieba.dt.initialize()
        self.t2s = opencc.OpenCC('t2s.json')

        def symbol2fixPinyin(pinyin):
            pinyin = replace_symbol_to_no_symbol(pinyin)
            fixed_pinyin = self.fixPinyin(pinyin)
            if fixed_pinyin is None or fixed_pinyin in initials_set:
                print(pinyin)
                assert False  # 库的拼音不规范，需要手动规范化
            return fixed_pinyin
        self.word_pinyin_s = {i:
            list(map(symbol2fixPinyin, pinyin_dict[i].split(',')))
            for i in pinyin_dict
            }

        """
            从 jieba 库里的 FREQ 得到所有字音的频率，转换得到：
                self.word_dict 所有字的字音频率字典，格式为
                    {
                        (字,音): 频,
                        (字,音): 频,
                        (字,音): 频,
                        ...
                    }
        """
        self.word_dict = {}
        for i in self.word_pinyin_s:
            word = chr(i)
            freq = jieba.dt.FREQ[word] if word in jieba.dt.FREQ else 1

            # 将多音字的第一个音设为 FREQ 里的频率
            self.word_dict[(word, self.word_pinyin_s[i][0])] = freq

            for pinyin in self.word_pinyin_s[i][1:]:
                # 将其它音的频率设为 1
                if (word, pinyin) not in self.word_dict:
                    self.word_dict[(word, pinyin)] = 1

        """
            self.phrase_r 所有词的频率信息字典，格式为
                {
                    词: 频,
                    词: 频,
                    词: 频,
                    ...
                }
        """
        self.phrase_r = {}

    def mergeDict(self, text, weight = 1, min_freq = 0, callbackCount = sys.maxsize, callbackFunc = None):
        """
            将 text 里储存的词频、字频内容合并到数据结构中
            text: 原始文本，会自动过滤掉拼音和其它字符
                原始文本的每一行格式为：
                    字或词组\t其它信息\t频率
            weight: 权值，该词库的频率乘以此权值再合并
            min_freq: 最小频率，小于该频率的词会被过滤掉
            返回值: 成功合并的数目元组，格式为 (word_count, parse_count)
        """

        word_count = 0
        parse_count = 0
        skip_count = 0

        text_s = text.split('\n')
        for line in text_s:
            v = tuple(map(lambda e:e.strip(), line.split('\t')))

            # 将最后一列视为频率，如果不是则默认为 1
            if not v[-1].isdigit():
                freq = weight  # 1 * weight
            else:
                freq = int(v[-1]) * weight

            # 过滤掉词频过小的词
            if freq < min_freq:
                skip_count += 1
                count = word_count + parse_count + skip_count
                if count % callbackCount == 0:
                    callbackFunc(count, len(text_s))
                continue

            # 将第一列视为汉字或词组，如果不是则跳过这一行（break）
            word = None
            for c in v[0]:
                if ord(c) not in self.word_pinyin_s:
                    break
            else:
                word = v[0]
            if word is None or len(word) == 0:
                continue

            # 当 word 为单字时，将第二列视为拼音，如果出错则设为该字的第一个拼音
            pinyin = None
            if len(word) == 1:
                if len(v) > 1:
                    if v[1].isalpha():
                        pinyin = self.fixPinyin(v[1])
                if pinyin is None:
                    pinyin = self.word_pinyin_s[ord(word)][0]

            # 如果是单字，则合并到 self.word_dict 里
            if len(word) == 1:
                word = self.t2s.convert(word)  # 确保字为简体
                key = (word, pinyin)
                if key in self.word_dict:
                    self.word_dict[key] += freq
                else:
                    sys.stderr.write('新的字音： %s\t%s\n' % key)
                word_count += 1

            # 如果是词组，则合并到 self.phrase_r 里
            else:
                word = self.t2s.convert(word)  # 确保词组为简体
                if word in self.phrase_r:
                    self.phrase_r[word] += freq
                else:
                    self.phrase_r[word] = freq
                parse_count += 1

            if callbackFunc is not None:
                count = word_count + parse_count + skip_count
                if count % callbackCount == 0:
                    callbackFunc(count, len(text_s))

        return (word_count, parse_count)


    def getWordDictText(self):
        """
            生成单字的 rime 字典文本
        """
        # 按频率倒序排序
        word_list = [(key[0], key[1], self.word_dict[key]) for key in self.word_dict]
        word_list.sort(key = lambda w: w[2], reverse = True)

        # 生成文本
        text_dict = ''
        for word_st in word_list:
            text_dict += word_st[0] + '\t' + word_st[1] + '\t' + str(word_st[2]) + '\n'
        return text_dict

    def getParseDictText(self, callbackCount = sys.maxsize, callbackFunc = None):
        """
            生成词组的 rime 字典文本
            由于词典量较大，所以需要显示转换进度
            callbackCount 为每过几个词调用一次 callbackFunc
            callbackFunc 是回调函数，自定义如何处理进度
                格式为 callbackFunc(count, total_count)
                    count 为当前已处理的个数
                    total_count 为总共数量
        """
        # 按频率倒序排序
        phrase_list = [(phrase, self.phrase_r[phrase]) for phrase in self.phrase_r]
        phrase_list.sort(key = lambda w: w[1], reverse = True)

        # 生成文本
        count = 0
        text_phrase = ''
        for phrase_st in phrase_list:
            # 通过 pypinyin 库获取到词组的拼音
            phrase_pinyin = map(self.fixPinyin, pypinyin.lazy_pinyin(phrase_st[0]))
            text_phrase += phrase_st[0] + '\t' + \
                ' '.join(phrase_pinyin) + '\t' + \
                str(phrase_st[1]) + '\n'
            count += 1
            if callbackFunc is not None:
                if count % callbackCount == 0:
                    callbackFunc(count, len(phrase_list))
        return text_phrase



def main(args):
    #text_dict, text_phrase = generate('clover')
    #open('clover.base.dict.yaml', 'w', encoding = 'UTF-8').write(text_dict)
    #open('clover.phrase.dict.yaml', 'w', encoding = 'UTF-8').write(text_phrase)
    generator = DictGenerator()

    class PrintProcess:
        def __init__(self, msg):
            self.msg = msg
        def process(self, count, total):
            print(self.msg % (count, total))

    # 合并 360万 的词库
    text = open('词典360万（个人整理）.txt', 'r', encoding = 'utf-8').read()
    r = generator.mergeDict(text, 1, args.minfreq, 100000,
        PrintProcess('正在合并360万中文词库 (%s/%s)').process)
    print('成功合并360万中文词库 %s 个汉字， %s 个词组。' % r)

    # 合并 rime 自带的八股文，权值 60
    text = open('essay.txt', 'r', encoding = 'utf-8').read()
    r = generator.mergeDict(text, 60, 0, 100000,
        PrintProcess('正在合并八股文 (%s/%s)').process)
    print('成功合并八股文 %s 个汉字， %s 个词组。' % r)

    # 合并袖珍简化字拼音的词库，权值 60
    text = open('pinyin_simp.dict.yaml', 'r', encoding = 'utf-8').read(
        ).replace('罗嗦', '啰嗦')
    r = generator.mergeDict(text, 60, 0, 100000,
        PrintProcess('正在合并袖珍简化字拼音的词库 (%s/%s)').process)
    print('成功合并袖珍简化字拼音 %s 个汉字， %s 个词组。' % r)

    # 合并转换符号词汇
    text = open('symbols.txt', 'r', encoding = 'utf-8').read()
    r = generator.mergeDict(text, 10000, 0, 100000,
        PrintProcess('正在合并符号词汇 (%s/%s)').process)
    print('成功合并符号词汇 %s 个汉字， %s 个词组。' % r)

    word_dict_name = 'clover.base'
    parse_dict_name = 'clover.phrase'

    word_dict_text = """
# Rime 字典
# encoding: utf-8
#
# 该字典生成的项目地址： https://github.com/fkxxyz/clover-dict-gen
#
# 所有文字的频率
# 生成自以下两个项目项目
#     结巴分词 https://github.com/fxsjy/jieba
#     rime 八股文 https://github.com/rime/rime-essay
#     袖珍简化字拼音 https://github.com/rime/rime-pinyin-simp
# 注音生成自 pypinyin 项目
#     https://github.com/mozillazg/python-pinyin
#

---
name: %s
version: "1.0.0"
sort: by_weight
...
""" % word_dict_name + generator.getWordDictText()

    parse_dict_text = """
# Rime 字典
# encoding: utf-8
#
# 该字典生成的项目地址： https://github.com/fkxxyz/clover-dict-gen
#
# 所有词组的频率
# 生成自以下三个项目项目
#     刘邵博的 360万中文词库+词性+词频
#     rime 八股文 https://github.com/rime/rime-essay
#     袖珍简化字拼音 https://github.com/rime/rime-pinyin-simp
# 注音生成自 pypinyin 项目
#     https://github.com/mozillazg/python-pinyin
#

---
name: %s
version: "1.0.0"
sort: by_weight
...
""" % parse_dict_name + generator.getParseDictText(
        10000,
        PrintProcess('正在取得每个词组的拼音 (%s/%s)').process)


    open(word_dict_name + '.dict.yaml', 'w').write(word_dict_text)
    open(parse_dict_name + '.dict.yaml', 'w').write(parse_dict_text)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Clover pinyin dict generator.")
    parser.add_argument('--minfreq', '-m',
        help='Specify the minimum frequency, ' + \
        'phrases that are less than this frequency will be filtered out',
        type=int, default=100)
    args = parser.parse_args()
    main(args)

