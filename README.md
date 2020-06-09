# 🍀️四叶草拼音输入法

## 简介

在linux端，很多拼音输入法有少许bug和卡顿，或功能不全，所以接触了 [rime](https://rime.im) ，然而自带的[朙月拼音](https://github.com/rime/rime-luna-pinyin)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)均不是很不是很理想，但是探索过程中发现很多很好的开源项目提供词库，那么我为什么不综合这些开源项目的优点基于 rime 制作出一个词库和配置呢。

## 定制描述

特色以及描述如下：

1. 自己做词库，包含词频信息，各个词库分开存放。

   - 用 [pypinyin](https://github.com/mozillazg/python-pinyin) 项目生成所有字词的拼音
   - 参考[结巴中文分词](https://github.com/fxsjy/jieba)项目和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)的字的字频

   - 由百度搜索到某个人基于大数据做过的[360万中文词库+词性+词频](https://download.csdn.net/download/xmp3x/8621683)

   - 自带[清华大学开源词库](https://github.com/thunlp/THUOCL)。
   
2. 加入 [emoji](https://github.com/rime/rime-emoji) 支持

3. 支持繁简切换，用 [opencc](https://github.com/BYVoid/OpenCC) 从简体切换为繁体

4. 让符号的输入符合搜狗拼音的习惯

5. 部分符号能够通过拼音输入，如 ²

   [rime-symbols](https://github.com/fkxxyz/rime-symbols) 该模块与此项目独立，你可以把这个模块放到别的输入法上用。

6. 实现一个词库设置工具，能够实现打patch，设置模糊音，导入词库等。

   （暂未实现）

如果你想了解此项目词库的具体生成过程，请来这两个地方： [clover-dict-gen](https://github.com/fkxxyz/clover-dict-gen) 和 [thuocl2rime](https://github.com/fkxxyz/thuocl2rime)

## 开始使用

由于 rime 是跨平台的，因此🍀️四叶草简体拼音也能在各个平台使用，所以请先参考 https://rime.im/download/ 安装好 rime 引擎，注意添加好 [emoji](https://github.com/rime/rime-emoji) 支持，再继续执行下面步骤。

克隆此仓库

```shell
git clone https://github.com/fkxxyz/rime-cloverpinyin.git
```

复制所有配置到目录，fcitx、ibus、小狼毫的配置目录均不同，下面以 fcitx 为例

```shell
cp rime-cloverpinyin/data/* ~/.config/fcitx/rime/
```

然后修改配置目录的 default.custom.yaml ，将此输入法加入列表

```shell
patch:
  schema_list/schema: clover
```

然后，切换到 rime 输入法，打开菜单点击重新部署即可（一般会自动重新部署），由于词库量大，第一次部署需要一定的时间耐心等待即可。

提示：默认按 F4 打开方案选单，再按 2，可以繁简切换、emoji开关、全角半角切换。

最后，有什么建议想法或者需要什么帮助，欢迎在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出。