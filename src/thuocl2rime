#!/usr/bin/env python
#-*- encoding:utf-8 -*-


import pypinyin

import argparse
import os
import sys

initials_set = set(pypinyin.style._constants._INITIALS)   # 声母表

def main(args):
    if not os.path.isfile(args.src):
        sys.stderr.out("文件 %s 不存在。" % args.src)
        return 1

    if args.dest is None:
        file_name = args.src[args.src.rfind(os.sep)+1:]
        dot_pos = file_name.rfind('.')
        if dot_pos == -1:
            args.dest = file_name + '.dict.yaml'
        else:
            args.dest = file_name[:dot_pos] + '.dict.yaml'

    if not args.dest.endswith('.dict.yaml'):
        sys.stderr.out("目标文件需要以 .dict.yaml 结尾")
        return 2
    name = args.dest[args.dest.rfind(os.sep)+1:][:-10]

    result = """name: %s
version: "1"
sort: by_weight

...
""" % name

    # 检查每个字都为合法汉字的字符串
    def checkPhrase(phrase):
        for c in phrase:
            if ord(c) not in pypinyin.pinyin_dict.pinyin_dict:
                return False
        return True

    text = open(args.src).read()
    for v in map(lambda x:x.split(), text.split('\n')):
        if len(v) == 2:
            # 检查该词组的每个字必须为汉字
            if not checkPhrase(v[0]):
                continue

            # 获取该词组的拼音
            pinyin = pypinyin.lazy_pinyin(v[0])
            for p in pinyin:
                if p in initials_set:  # 拼音不能只包含声母
                    break
            else:
                result += v[0] + '\t' + ' '.join(pinyin) + '\t' + v[1] + '\n'

    open(args.dest, 'w').write(result)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = \
        "将清华大学开放中文词库转换为 rime 的词库格式 .dict.yaml")
    parser.add_argument('src', help = \
        '清华大学开放中文词库文件，一般形如 THUOCL_xx.txt')
    parser.add_argument('dest', help = \
        '目标文件路径，注意要以 .dict.yaml 结尾，' + \
        '如果此参数省略，则会在当前目录下生成同名的 .dict.yaml 文件。',
        nargs='?')

    args = parser.parse_args()
    
    exit(main(args))
