# 🍀️四叶草拼音输入方案

## 简介

在linux端，很多拼音输入法有少许bug和卡顿，或功能不全，所以接触了 [rime](https://rime.im) ，然而自带的[朙月拼音](https://github.com/rime/rime-luna-pinyin)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)均不是很不是很理想，但是探索过程中发现很多很好的开源项目提供词库，那么我为什么不综合这些开源项目的优点基于 rime 制作出一个词库和配置呢。

## 定制描述

特色以及描述如下：

1. 自己做词库，包含词频信息，各个词库分开存放。

   - 用 [pypinyin](https://github.com/mozillazg/python-pinyin) 项目生成所有字词的拼音
   - 参考[结巴中文分词](https://github.com/fxsjy/jieba)项目、[rime八股文](https://github.com/rime/rime-essay)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)的字的字频

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

由于 rime 是跨平台的，因此🍀️四叶草简体拼音也能在各个平台使用，所以请先参考 https://rime.im/download/ 安装好 rime 引擎，然后在 [releases](https://github.com/fkxxyz/rime-cloverpinyin/releases) 界面下载最新版本的 **clover.schema-版本号.zip** 或 **clover.schema-build-版本号.zip** ，解压到[用户资料目录](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E4%B8%AD%E7%9A%84%E6%95%B8%E6%93%9A%E6%96%87%E4%BB%B6%E5%88%86%E4%BD%88%E5%8F%8A%E4%BD%9C%E7%94%A8)。

clover.schema 和 clover.schema-build 的区别是
- **clover.schema** 不包含二进制文件，复制到新机器上之后需要重新部署。
- **clover.schema-build** 包含二进制文件目录（build目录），复制到新机器上之后重新部署的时间大量缩短。

然后修改配置目录的 default.custom.yaml ，将此输入法加入列表（小狼毫可以直接点右下角右键，输入法设定可以直接勾选）

```shell
patch:
  schema_list/schema: clover
```

然后，切换到 rime 输入法，打开菜单点击重新部署即可（一般会自动重新部署），由于词库量大，第一次部署需要一定的时间耐心等待即可。

提示：默认按 F4 打开方案选单，再按 2，可以繁简切换、emoji开关、特殊符号开关、全角半角切换。

最后，有什么建议想法或者需要什么帮助，欢迎在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出。

## 关于构建

该仓库的内容只包含构建四叶草输入法方案的脚本，如果想要自己构建，需要以下环境

操作系统： linux

python版本： 3

python依赖的库： [jieba](https://github.com/fxsjy/jieba)、[pypinyin](https://github.com/mozillazg/python-pinyin)、[opencc](https://github.com/BYVoid/OpenCC)

下载工具（三者任意一个均可）： [aria2](http://aria2.sourceforge.net/)、[wget](https://www.gnu.org/software/wget/wget.html)、[curl](https://curl.haxx.se/)

解压工具（三者任意一个均可）： [unzip](https://www.info-zip.org/UnZip.html)、[bsdtar](https://libarchive.org/)、[7z](http://p7zip.sourceforge.net/)

rime基础库： [librime](https://github.com/rime/librime)

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

