你是否经历过搜狗输入法总是闪退bug的绝望？

你是否经历过 fcitx 自带输入法的词库简陋？

你是否经历过在 linux 中尝试各种输入法都不理想呢？

这里是帮你脱离苦海的地方。

<!--more-->

# :four_leaf_clover:四叶草拼音输入方案


## 简介

在linux端，很多拼音输入法有少许 bug 或卡顿，或功能不全，所以接触了 [rime](https://rime.im) ，然而自带的[朙月拼音](https://github.com/rime/rime-luna-pinyin)和[袖珍简化字拼音](https://github.com/rime/rime-pinyin-simp)均不是很不是很理想，但是探索过程中发现很多很好的开源项目提供词库，而 rime 输入法引擎几乎拥有所有的优点（开源、干净无广告、运行流畅、跨平台、...），甚至云同步也能用坚果云之类的服务手动实现，唯一的缺点就是门槛高定制困难，默认配置的不习惯劝退了很多人。

在此方案诞生之前，我没能找到一个比较不错的简体拼音（全拼）的输入方案，多数人用惯了大陆国产的输入法，而以我的动手能力，完全能够按照这些输入法的习惯，自己定制一个方案，共享给更多的人，让更多的人不需要怎么配置也能用上非常类似于搜狗拼音输入法的方案，尽可能开箱即用，降低所有人的使用门槛。所以，为什么不自己做一个呢？

**这个项目我会持续更新，因为我一直在用输入法，我会调教到完全合我的口味习惯为止（我过去一直在用搜狗拼音输入法）。所以如果你觉得哪里不好用，或者哪里想改善，一定要及时在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出，我只要看到就会回复。**

- 博文地址	https://www.fkxxyz.com/d/cloverpinyin

- 项目地址	https://github.com/fkxxyz/rime-cloverpinyin

## 特色

我亲自打造的基于[rime](https://rime.im/)的简体拼音输入方案，有以下几大特点：

1. 完全从零开始制作文字的拼音和基础词库，导入了几个很好用的词库：

   - 用 [pypinyin](https://github.com/mozillazg/python-pinyin) 项目生成所有字词的拼音
   - 合并[结巴中文分词](https://github.com/fxsjy/jieba)项目、[rime八股文](https://github.com/rime/rime-essay)和[袖珍简化字拼音](https://github.com/rime/rime-pinyin-simp)的字的字频
   - 由百度搜索到某个人基于大数据做过的[360万中文词库+词性+词频](https://download.csdn.net/download/xmp3x/8621683)，该词库是用ansj分词对270G新闻语料进行分词统计词频获得
   - [清华大学开源词库](https://github.com/thunlp/THUOCL)，统计来自各大主流网站如CSDN博客、新浪新闻、搜狗语料
   - 搜狗细胞词库 [网络流行新词【官方推荐】](https://pinyin.sogou.com/dict/detail/index/4)
  
2. 词库本身基于简体，并且加入繁简切换，包括自定义词库也能切换繁体（朙月拼音输入简体时的需要经过opencc转换，而且自定义词库也得手动转换成繁体才能繁简切换，而袖珍简化字拼音不支持繁体）

3. 默认加入 emoji 表情输入支持

   ![](https://www.fkxxyz.com/img/cloverpinyin-1.png)

4. 加入拼音输入特殊符号的支持（如输入 pingfang 即可打出 ²）

   ![](https://www.fkxxyz.com/img/cloverpinyin-2.png)

   [rime-symbols](https://github.com/fkxxyz/rime-symbols) 该模块与此项目独立，你也可以把这个模块放到别的方案上用。

5. 修改了几乎所有特殊符号的按键，定制全部快捷键，使之符合搜狗输入法的习惯

不磨蹭了，直接介绍怎么开始使用吧。

## 安装

安装说明已迁移到本项目的 wiki，详见：

[安装说明](https://github.com/fkxxyz/rime-cloverpinyin/wiki/Home)

- [在 Windows 下使用](https://github.com/fkxxyz/rime-cloverpinyin/wiki/windows)
- [在 Linux 下使用](https://github.com/fkxxyz/rime-cloverpinyin/wiki/linux)

## 从本仓库源码构建

一般情况下，我在发布页提供的是已经生成好的词库和部署好的二进制文件，直接使用即可。

如果你想自己从零开始构建，或者想为别的 linux 发行版打包，那么继续往下看。

该仓库的内容只包含构建四叶草输入法方案的脚本，构建需要以下环境

操作系统： linux

python版本： 3

python依赖的库： [jieba](https://github.com/fxsjy/jieba)、[pypinyin](https://github.com/mozillazg/python-pinyin)、[opencc](https://github.com/BYVoid/OpenCC)、requests

下载工具（三者任意一个均可）： [aria2](http://aria2.sourceforge.net/)、[wget](https://www.gnu.org/software/wget/wget.html)、[curl](https://curl.haxx.se/)

解压工具（三者任意一个均可）： [unzip](https://www.info-zip.org/UnZip.html)、[bsdtar](https://libarchive.org/)、[7z](http://p7zip.sourceforge.net/)

rime基础库： [librime](https://github.com/rime/librime)

rime基础配置： [librime-prelude](https://github.com/rime/rime-prelude)

克隆此仓库，然后直接执行构建即可

```shell
./build
```

完成后，会生成 cache 目录和 data 目录

- data 是最终生成的目录
- cache 是生成过程中下载和生成的中间文件



其中，执行 build 时，可以有个参数

```shell
./build [minfreq]
```

minfreq 代表360万词里面指定的最小词频，频率低于该值的词语会被筛选掉，达到精简词库的目的，默认是100，该值越小，最终生成的词库越大，为 0 表示不精简词库（会生成大约 100 兆左右的词库）。

构建完成后，可以打包，在 data 目录生成发布用的压缩包

```
./pack [ver]
```

ver 表示版本号，例如 1.1.2

---

## 写在最后

此项目完全开源，你可以随意 fork 或修改和定制，如果你觉得好用，可以来[AUR投票](https://aur.archlinux.org/packages/rime-cloverpinyin/)和在[github上star](https://github.com/fkxxyz/rime-cloverpinyin)，投票和star的人越多越容易被搜索到，以此更好地传播出去。

再次重复开头说的：

**这个项目我会持续更新，因为我一直在用输入法，我会调教到完全合我的口味习惯为止（我过去一直在用搜狗拼音输入法）。所以如果你觉得哪里不好用，或者哪里想改善，一定要及时在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出，我只要看到就会回复。**

当然你也可以直接[联系我](https://www.fkxxyz.com/about/#%E5%85%B3%E4%BA%8E%E6%88%91)本人。

