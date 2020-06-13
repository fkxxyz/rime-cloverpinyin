---
title: 再也不用为中文输入法而烦恼了
cover: false
date: 2020-06-10 07:28:01
categories:
- 原创开发
tags:
- rime
- fcitx
- 输入法
typora-root-url: ../..
---

你是否经历过搜狗输入法总是闪退bug的绝望？

你是否经历过 fcitx 自带输入法的词库简陋？

你是否经历过在 linux 中尝试各种输入法都不理想呢？

这里是帮你脱离苦海的地方。

<!--more-->

## 简介

在linux端，很多拼音输入法有少许 bug 或卡顿，或功能不全，所以接触了 [rime](https://rime.im) ，然而自带的[朙月拼音](https://github.com/rime/rime-luna-pinyin)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)均不是很不是很理想，但是探索过程中发现很多很好的开源项目提供词库，而 rime 输入法引擎几乎拥有所有的优点（开源、干净无广告、运行流畅、跨平台、...），甚至云同步也能用坚果云之类的服务手动实现，唯一的缺点就是门槛高定制困难，默认配置的不习惯劝退了很多人。

在此方案诞生之前，我没能找到一个比较不错的简体拼音（全拼）的输入方案，多数人用惯了大陆国产的输入法，而以我的动手能力，完全能够按照这些输入法的习惯，自己定制一个方案，共享给更多的人，让更多的人不需要怎么配置也能用上非常类似于搜狗拼音输入法的方案，尽可能开箱即用，降低所有人的使用门槛。所以，为什么不自己做一个呢？

**这个项目我会持续更新，因为我一直在用输入法，我会调教到完全合我的口味习惯为止（我过去一直在用搜狗拼音输入法）。所以如果你觉得哪里不好用，或者哪里想改善，一定要及时在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出，我只要看到就会回复。**

项目地址：

- **github**	https://github.com/fkxxyz/rime-cloverpinyin

## 特色

我亲自打造的基于[rime](https://rime.im/)的简体拼音输入方案，有以下几大特点：

1. 完全从零开始制作文字的拼音和基础词库，导入了几个很好用的开源词库：

   - 用 [pypinyin](https://github.com/mozillazg/python-pinyin) 项目生成所有字词的拼音
   - 合并[结巴中文分词](https://github.com/fxsjy/jieba)项目、[rime八股文](https://github.com/rime/rime-essay)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)的字的字频

   - 由百度搜索到某个人基于大数据做过的[360万中文词库+词性+词频](https://download.csdn.net/download/xmp3x/8621683)

   - [清华大学开源词库](https://github.com/thunlp/THUOCL)。

2. 加入繁简切换，包括自定义词库也能切换繁体（这在rime官方默认配置是没有现成的）

3. 默认加入 emoji 表情输入支持

   ![](https://www.fkxxyz.com/img/cloverpinyin-1.png)

4. 加入拼音输入特殊符号的支持（如输入 pingfang 即可打出 ²）

   ![](https://www.fkxxyz.com/img/cloverpinyin-2.png)

   [rime-symbols](https://github.com/fkxxyz/rime-symbols) 该模块与此项目独立，你也可以把这个模块放到别的方案上用。

5. 修改了几乎所有特殊符号的按键，使之符合搜狗输入法的习惯

不磨蹭了，直接介绍怎么开始使用吧。

## 开始

rime 是跨平台的，在以下四个平台可用：

- **linux** 可以使用 fcitx、fxitx5、ibus

- **windows** 使用小狼毫

- **macOS** 可以用鼠鬚管

- **安卓** 使用同文输入法

这些软件如果你想在这些平台使用，可以具体参照官方的[下载安装说明](https://rime.im/download/)

---

下面介绍在 linux 和 windows 端如何安装。

### linux端( fcitx )

#### 安装 fcitx

在 archlinux 下：

```shell
pacman -S fcitx fcitx-qt5 fcitx-configtool
```

然后配置 fcitx 的环境变量

在 ~/.xprofile 写入

```shell
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"

export LANG="zh_CN.UTF-8"
export LC_CTYPE="zh_CN.UTF-8"
```



其他发行版的安装参见 [小企鹅官网安装配置方法](https://fcitx-im.org/wiki/Install_and_Configure/zh-hans)



安装和配置完成后，记得重新登录桌面使之生效。



#### 安装 rime

在 archlinux 下，安装 rime：

```shell
pacman -S fcitx-rime
```

其他发行版请用相应的包管理器安装，详见 https://rime.im/download/



#### 安装🍀️四叶草输入方案

在 archlinux 下，可以从 [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 直接安装即可：

```shell
yay -S fcitx-cloverpinyin
```

在其它发行版下，来发布页 https://github.com/fkxxyz/rime-cloverpinyin/releases 下载最新版本的配置文件，如 clover.schema-1.1.0.zip

然后将其解压到 ~/.config/fcitx/rime

创建 ~/.config/fcitx/rime/default.custom.yaml ，内容为

```yaml
patch:
  "menu/page_size": 8
  schema_list:
    - schema: clover
```

其中 8 表示打字的时候输入面板的每一页的候选词数目，可以设置成 1~9 任意数字。

写好该文件之后，点击右下角托盘图标右键菜单，点“重新部署”，然后再点右键，在方案列表里面应该就有“ 🍀️四叶草拼音输入法”的选项了。

关于 default.custom.yaml 文件的更多解释，可以参考[官方文档定制指南](https://github.com/rime/home/wiki/CustomizationGuide)



#### 美观

关于 fcitx 的皮肤，可以参考这里：

[原来 fcitx 也可以这么美 —— 对 fcitx 使用搜狗皮肤的改进](https://www.fkxxyz.com/d/ssfconv/)

### windows端（小狼毫）

#### 下载安装小狼毫

来 [rime下载页](https://rime.im/download/) 下载最新版本的小狼毫（注意 Windows XP 只最高只能下载 0.12.0），然后按照提示进行安装。

#### 下载输入方案

来发布页 https://github.com/fkxxyz/rime-cloverpinyin/releases 下载最新版本的配置文件，如 clover.schema-1.1.0.zip

然后将其解压到 %appdata%/rime 即可（如果你更改了用户配置目录，那么解压到对应目录即可）。

然后切换到中州韵输入法，右键托盘图标，点击输入法设定，勾选上四叶草输入方案，确定，再点右键托盘图标，重新部署，等待数分钟后，即可使用。

#### 美观

小狼毫的字体、配色方案参考 [官方配置指南--小狼毫](https://github.com/rime/home/wiki/CustomizationGuide#一例定製小狼毫字體字號)

### 关于发布页

由于 rime 处理词库的原理是提前将词库转换为二进制文件，这个过程成为部署，所以我在[发布页](https://github.com/fkxxyz/rime-cloverpinyin/releases)提供了两个压缩包，一个包含二进制文件，一个不包含二进制文件。

- **clover.schema** 不包含二进制文件，复制到新机器上之后需要重新部署。
- **clover.schema-build** 包含二进制文件目录（build目录），复制到新机器上之后重新部署的时间大量缩短。

### 关于rime的配置

所有配置都围绕着用户资料夹展开，参考 [Rime 中的數據文件分佈及作用](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E4%B8%AD%E7%9A%84%E6%95%B8%E6%93%9A%E6%96%87%E4%BB%B6%E5%88%86%E4%BD%88%E5%8F%8A%E4%BD%9C%E7%94%A8)

另外，需要注意 rime 的配置文件严格遵守 yaml 语法，缩进都是两个空格，不能用 tab 代替，否则配置是无效的（很多人折腾死在这）

### 候选词个数

修改用户资料夹的 default.custom.yaml ，找到 menu/page_size 字段，如果没有则创建，设置该字段的值即可。例如

```yaml
patch:
  "menu/page_size": 8
  schema_list:
    - schema: clover
```

详见 [一例、定製每頁候選數](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E6%AF%8F%E9%A0%81%E5%80%99%E9%81%B8%E6%95%B8)

### 模糊音

对于模糊音的配置，目前还没有方便的图形界面的配置，如果有需要的话照做吧：

在用户资料夹创建 clover.custom.yaml ，内容为

```yaml
patch:
  speller/algebra:

    # 模糊音

    # 基础
    - abbrev/^([a-z]).+$/$1/
    - abbrev/^([zcs]h).+$/$1/
    
    # 补全
    - derive/([dtngkhrzcs])o(u|ng)$/$1o/   # o = ou; o = ong
    - derive/ong$/on/      # on = ong
    - derive/^ding$/din/     # din = ding
    
    # 处理 v 和 u
    - derive/^([nl])ue$/$1ve/   # nve = nue; lve = lue
    - derive/^([jqxy])u/$1v/    # v = u; v = u
    
    # 智能纠错
    - derive/ao$/oa/       # oa = ao
    - derive/([iu])a(o|ng?)$/a$1$2/   # aio = iao; aing = iang; aung = uang
    - derive/([aeiou])ng$/$1gn/   # gn = ng
    - derive/un$/uen/    # uen = un
    - derive/ui$/uei/    # uei = ui
    - derive/iu$/iou/    # iou = ui
    - derive/tie$/tei/    # tei = tie
    - derive/([bpmfdtnlgkhjqxzcsryw])([iu])/$2$1/   # u和i不小心提前
    - derive/i$/ii/      # ii = i  # i 不小心按两下
    - derive/u$/uu/      # ui = u  # u 不小心按两下
```

然后参考官方推荐的模糊音配置 https://gist.github.com/lotem/2320943

找到你想添加的模糊音，在第三行前面加上即可。

再次强调 yaml 的语法，上面每个 derive 前面都是四个空格，不能用 tab 代替。

如，我想把 en 与 eng 和 in 与 ing 模糊，那么修改后就变成了这样：

```yaml
patch:
  speller/algebra:

    # 模糊音
    - derive/([ei])n$/$1ng/    # ing = in; eng = en
    - derive/([ei])ng$/$1n/    # in = ing; en = eng

    # 基础
    - abbrev/^([a-z]).+$/$1/
    - abbrev/^([zcs]h).+$/$1/
    
    # 补全
    - derive/([dtngkhrzcs])o(u|ng)$/$1o/   # o = ou; o = ong
    - derive/ong$/on/      # on = ong
    - derive/^ding$/din/     # din = ding
    
    # 处理 v 和 u
    - derive/^([nl])ue$/$1ve/   # nve = nue; lve = lue
    - derive/^([jqxy])u/$1v/    # v = u; v = u
    
    # 智能纠错
    - derive/ao$/oa/       # oa = ao
    - derive/([iu])a(o|ng?)$/a$1$2/   # aio = iao; aing = iang; aung = uang
    - derive/([aeiou])ng$/$1gn/   # gn = ng
    - derive/un$/uen/    # uen = un
    - derive/ui$/uei/    # uei = ui
    - derive/iu$/iou/    # iou = ui
    - derive/tie$/tei/    # tei = tie
    - derive/([bpmfdtnlgkhjqxzcsryw])([iu])/$2$1/   # u和i不小心提前
    - derive/i$/ii/      # ii = i  # i 不小心按两下
    - derive/u$/uu/      # ui = u  # u 不小心按两下
```

当然如果你能看懂上面的正则表达式，那么你也可以自己自定义模糊音了。

修改完成后，记得重新部署生效。

### 繁简切换、emoji、符号输入

由于 rime 的设定，繁简切换等需要打开方案选单来完成，方案选单默认有个快捷键 F4 ，按 F4，再按 2，即可看到一些设定，选择相应的开关设定即可。

这个快捷键可以修改，详见 [一例、定製喚出方案選單的快捷鍵](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E5%96%9A%E5%87%BA%E6%96%B9%E6%A1%88%E9%81%B8%E5%96%AE%E7%9A%84%E5%BF%AB%E6%8D%B7%E9%8D%B5)

### 目前不足

有时候，发现以为自己最经常打的字候选词里一定排在第一位，但是时间长了发现好像并不是这么回事，似乎自己最近打的词比使用频率最高的词排序还要靠前，这导致大量的输入错误严重降低了打字效率，后来看到这个帖子

[『技术贴』『改进版』小狼毫五笔自动造词、网盘同步](https://tieba.baidu.com/p/5085900915)

原来 rime 的排序特点就是如此，但是这会导致词序经常很乱，也无法固定首位，怎么办呢，自己改代码！

后续我会将改好的 patch 发布，以及发布探索如何改代码的博文。

## 自己构建词库

我在发布页提供的是已经生成好的词库和部署好的二进制文件，直接使用即可。

该仓库的内容只包含构建四叶草输入法方案的脚本，如果你想要自己从零构建词库，需要以下环境

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



---

## 写在最后

此项目完全开源，你可以随意 fork 或修改和定制，如果你觉得好用，可以来[AUR投票](https://aur.archlinux.org/packages/rime-cloverpinyin/)和在[github上star](https://github.com/fkxxyz/rime-cloverpinyin)，投票和star的人越多越容易被搜索到，以此更好地传播出去。

再次重复开头说的：

**这个项目我会持续更新，因为我一直在用输入法，我会调教到完全合我的口味习惯为止（我过去一直在用搜狗拼音输入法）。所以如果你觉得哪里不好用，或者哪里想改善，一定要及时在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出，我只要看到就会回复。**

当然你也可以直接[联系我](https://www.fkxxyz.com/about/#%E5%85%B3%E4%BA%8E%E6%88%91)本人。

