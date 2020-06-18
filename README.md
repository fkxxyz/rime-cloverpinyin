你是否经历过搜狗输入法总是闪退bug的绝望？

你是否经历过 fcitx 自带输入法的词库简陋？

你是否经历过在 linux 中尝试各种输入法都不理想呢？

这里是帮你脱离苦海的地方。

<!--more-->

## 目录

<!--ts-->
      * [目录](#目录)
      * [简介](#简介)
      * [特色](#特色)
      * [开始](#开始)
         * [linux端( fcitx )](#linux端-fcitx-)
            * [安装 fcitx](#安装-fcitx)
            * [安装 rime](#安装-rime)
            * [安装<g-emoji class="g-emoji" alias="four_leaf_clover" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f340.png">🍀️</g-emoji>四叶草输入方案](#安装️四叶草输入方案)
            * [美观](#美观)
         * [windows端（小狼毫）](#windows端小狼毫)
            * [下载安装小狼毫](#下载安装小狼毫)
            * [下载输入方案](#下载输入方案)
            * [美观](#美观-1)
            * [候选横排](#候选横排)
         * [关于发布页](#关于发布页)
      * [基本配置](#基本配置)
         * [候选词个数](#候选词个数)
         * [模糊音](#模糊音)
      * [常见问题](#常见问题)
         * [各种快捷键](#各种快捷键)
         * [出现候选框时按 Shift 字母不会上屏](#出现候选框时按-shift-字母不会上屏)
         * [删除一个自造词](#删除一个自造词)
         * [词序总是错乱](#词序总是错乱)
         * [emoji 字体呈方块状](#emoji-字体呈方块状)
         * [同步词库](#同步词库)
         * [其它](#其它)
      * [构建](#构建)
      * [写在最后](#写在最后)
<!--te-->

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

## 简介

在linux端，很多拼音输入法有少许 bug 或卡顿，或功能不全，所以接触了 [rime](https://rime.im) ，然而自带的[朙月拼音](https://github.com/rime/rime-luna-pinyin)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)均不是很不是很理想，但是探索过程中发现很多很好的开源项目提供词库，而 rime 输入法引擎几乎拥有所有的优点（开源、干净无广告、运行流畅、跨平台、...），甚至云同步也能用坚果云之类的服务手动实现，唯一的缺点就是门槛高定制困难，默认配置的不习惯劝退了很多人。

在此方案诞生之前，我没能找到一个比较不错的简体拼音（全拼）的输入方案，多数人用惯了大陆国产的输入法，而以我的动手能力，完全能够按照这些输入法的习惯，自己定制一个方案，共享给更多的人，让更多的人不需要怎么配置也能用上非常类似于搜狗拼音输入法的方案，尽可能开箱即用，降低所有人的使用门槛。所以，为什么不自己做一个呢？

**这个项目我会持续更新，因为我一直在用输入法，我会调教到完全合我的口味习惯为止（我过去一直在用搜狗拼音输入法）。所以如果你觉得哪里不好用，或者哪里想改善，一定要及时在 [issues](https://github.com/fkxxyz/rime-cloverpinyin/issues) 提出，我只要看到就会回复。**

- 博文地址	https://www.fkxxyz.com/d/cloverpinyin

- 项目地址	https://github.com/fkxxyz/rime-cloverpinyin

## 特色

我亲自打造的基于[rime](https://rime.im/)的简体拼音输入方案，有以下几大特点：

1. 完全从零开始制作文字的拼音和基础词库，导入了几个很好用的词库：

   - 用 [pypinyin](https://github.com/mozillazg/python-pinyin) 项目生成所有字词的拼音
   - 合并[结巴中文分词](https://github.com/fxsjy/jieba)项目、[rime八股文](https://github.com/rime/rime-essay)和[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)的字的字频
- 由百度搜索到某个人基于大数据做过的[360万中文词库+词性+词频](https://download.csdn.net/download/xmp3x/8621683)，该词库是用ansj分词对270G新闻语料进行分词统计词频获得
   - [清华大学开源词库](https://github.com/thunlp/THUOCL)，统计来自各大主流网站如CSDN博客、新浪新闻、搜狗语料
- 搜狗细胞词库 [网络流行新词【官方推荐】](https://pinyin.sogou.com/dict/detail/index/4)
  
2. 词库本身基于简体，并且加入繁简切换，包括自定义词库也能切换繁体（朙月拼音输入简体时的需要经过opencc转换，而且自定义词库也得手动转换成繁体才能繁简切换，而袖珍簡化字拼音不支持繁体）

3. 默认加入 emoji 表情输入支持

   ![](https://www.fkxxyz.com/img/cloverpinyin-1.png)

4. 加入拼音输入特殊符号的支持（如输入 pingfang 即可打出 ²）

   ![](https://www.fkxxyz.com/img/cloverpinyin-2.png)

   [rime-symbols](https://github.com/fkxxyz/rime-symbols) 该模块与此项目独立，你也可以把这个模块放到别的方案上用。

5. 修改了几乎所有特殊符号的按键，定制全部快捷键，使之符合搜狗输入法的习惯

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

#### 候选横排

候选词默认展示是竖排的，如果你习惯于横排展示候选词，请看 [【小狼毫】外觀設定](https://github.com/rime/home/wiki/CustomizationGuide#%E5%B0%8F%E7%8B%BC%E6%AF%AB%E5%A4%96%E8%A7%80%E8%A8%AD%E5%AE%9A)

方便起见，在此也附上网页版的配置链接 [RIME西米](https://bennyyip.github.io/Rime-See-Me/)

### 关于发布页

由于 rime 处理词库的原理是提前将词库转换为二进制文件，这个过程成为部署，所以我在[发布页](https://github.com/fkxxyz/rime-cloverpinyin/releases)提供了两个压缩包，一个包含二进制文件，一个不包含二进制文件。

- **clover.schema** 不包含二进制文件，复制到新机器上之后需要重新部署。
- **clover.schema-build** 包含二进制文件目录（build目录），复制到新机器上之后重新部署的时间大量缩短。

## 基本配置

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
    - derive/i$/ii/      # ii = i  # i 不小心按两下
    - derive/u$/uu/      # ui = u  # u 不小心按两下
```

当然如果你能看懂上面的正则表达式，那么你也可以自己自定义模糊音了。

修改完成后，记得重新部署生效。

## 常见问题

### 各种快捷键

该方案的默认快捷键为：

- 繁简切换	Ctrl+Shift+2 或 Ctrl+Shift+f 。
- emoji开关	Ctrl+Shift+3
- 符号输入	Ctrl+Shift+4
- ascii标点切换	Ctrl+Shift+5 、 Ctrl+,  或 Ctrl+。
- 全半角切换	Ctrl+Shift+6 、 Shift+Space

由于 rime 的设定，这些切换也可以通过打开方案选单来完成，方案选单默认有个快捷键 F4 ，按 F4，再按 2，即可看到这些设定，选择相应的开关设定即可。

这个快捷键可以修改，详见 [一例、定製喚出方案選單的快捷鍵](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E5%96%9A%E5%87%BA%E6%96%B9%E6%A1%88%E9%81%B8%E5%96%AE%E7%9A%84%E5%BF%AB%E6%8D%B7%E9%8D%B5)

如果你不想用 emoji 或者符号输入的功能，则需要修改配置文件才能永久关闭该功能：

修改 clover.custom.yaml ，添加一个补丁：

```yaml
  switches:
    - name: zh_simp_s2t
      reset: 0
      states: [ 简, 繁 ]
    - name: emoji_suggestion
      reset: 1
      states: [ "🈚️️\uFE0E", "🈶️️\uFE0F" ]
    - name: symbol_support
      reset: 1
      states: [ "无符", "符" ]
    - name: ascii_punct
      reset: 0
      states: [ 。，, ．， ]
    - name: full_shape
      reset: 0
      states: [ 半, 全 ]
    - name: ascii_mode
      reset: 0
      states: [ 中, 英 ]
```

将 emoji_suggestion 或 symbol_support 里面的 reset 改成 0 即可。

这里其实是定制方案选单的选项，reset 表示默认选中 states 的第几个选项，更多请看[一例、定製簡化字輸出](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E7%B0%A1%E5%8C%96%E5%AD%97%E8%BC%B8%E5%87%BA)

### 出现候选框时按 Shift 字母不会上屏

由于 rime 的中英文切换的快捷键和 fcitx 的切换输入法的快捷键都是 shift ，fcitx 的快捷键优先于 rime，所以会导致这种情况。

解决方法：右键托盘图标，配置，打开 fcitx 的配置，点全局配置，额外的激活输入法快捷键，选择禁用。点显示高级选项，在这里的激活输入法可以设置为 shift

### 删除一个自造词

有时候错误的输入了一个词语，这个错误的词语每次会出现在候选框中，看着难过，那么可以删除这个词语。

按上下键高亮选中这个词语，然后按 Ctrl+Del 或 Shift+Del即可删除该词。（鼠须管的快捷键是 Fn + Shift + Delete）

### 词序总是错乱

有时候，发现以为自己最经常打的字候选词里一定排在第一位，但是时间长了发现好像并不是这么回事，似乎自己最近打的词比使用频率最高的词排序还要靠前，这导致大量的输入错误严重降低了打字效率，后来看到这个帖子

[『技术贴』『改进版』小狼毫五笔自动造词、网盘同步](https://tieba.baidu.com/p/5085900915)

原来 rime 的排序特点就是如此，但是这会导致词序经常很乱，也无法固定首位，怎么办呢，我就这个问题向rime作者反馈，得到的回应是，这是记忆力算法，刚开始词序可能会变化较大，长期会趋于稳定，那这么看来暂时先这样用着时间长就好了。

rime作者的[回应](https://github.com/rime/librime/issues/377#issuecomment-644682195)是，这是记忆力算法，刚开始词序可能会变化较大，长期会趋于稳定，那这么看来暂时先这样用着时间长就好了。

后续我会将改好的 patch 发布，以及发布探索如何改代码的博文。

### emoji 字体呈方块状

这是因为没有安装 emoji 字体导致。

在 archlinux 下，可以直接从 aur 安装 apple emoji 的字体：

``` shell
yay -S ttf-apple-emoji
```

在其它 linux 发行版，可以从这个地址下载到 apple emoji 的字体

https://git.synh.me/dmitry/AUR/-/raw/master/files/ttf-apple-emoji/apple-color-emoji.ttc

下载好之后，需要复制到 /usr/share/fonts 的某个子目录下，然后更新字体缓存

```shell
cd /usr/share/fonts
sudo fonts.dir
sudo mkfontdir
```



在其它平台，需要自己想办法了。

### 同步词库

rime 允许不同系统之间进行词库的同步。

该功能详见 [同步用戶資料](https://github.com/rime/home/wiki/UserGuide#%E5%90%8C%E6%AD%A5%E7%94%A8%E6%88%B6%E8%B3%87%E6%96%99)

默认同步的文件夹在用户资料夹下 sync ，点击同步时，会生成这个文件夹，你也可以设置 installation.yaml 里面的 sync_dir 来修改同步文件夹。

用户词库词频信息被保存在 同步文件夹下的对应 id 里的 clover.userdb.txt 里，每次点击同步时，会合并所有 id 里的该文件。

所以可以利用云同步服务例如 [坚果云](https://www.jianguoyun.com/) 一类的软件，来实现个人不同电脑之间的词库同步。

### 其它

其它常见问题看[官方文档的常见问题](https://github.com/rime/home/wiki/CustomizationGuide#diy-%E8%99%95%E6%96%B9%E9%9B%86)吧。

## 构建

一般情况下，我在发布页提供的是已经生成好的词库和部署好的二进制文件，直接使用即可。

如果你想自己从零开始构建，或者想为别的 linux 发行版打包，那么继续往下看。

该仓库的内容只包含构建四叶草输入法方案的脚本，构建需要以下环境

操作系统： linux

python版本： 3

python依赖的库： [jieba](https://github.com/fxsjy/jieba)、[pypinyin](https://github.com/mozillazg/python-pinyin)、[opencc](https://github.com/BYVoid/OpenCC)、requests

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

