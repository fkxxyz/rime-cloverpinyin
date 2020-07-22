你是否经历过搜狗输入法总是闪退bug的绝望？

你是否经历过 fcitx 自带输入法的词库简陋？

你是否经历过在 linux 中尝试各种输入法都不理想呢？

这里是帮你脱离苦海的地方。

<!--more-->

# :four_leaf_clover:四叶草拼音输入方案



目录
=================

   * [:four_leaf_clover:四叶草拼音输入方案](#four_leaf_clover四叶草拼音输入方案)
   * [目录](#目录)
      * [简介](#简介)
      * [特色](#特色)
      * [开始](#开始)
         * [linux端( fcitx )](#linux端-fcitx-)
            * [安装 fcitx](#安装-fcitx)
            * [安装 rime](#安装-rime)
            * [安装:four_leaf_clover:四叶草输入方案](#安装four_leaf_clover四叶草输入方案)
            * [切换到:four_leaf_clover:四叶草输入方案](#切换到four_leaf_clover四叶草输入方案)
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
         * [导入自定义词库](#导入自定义词库)
            * [基本步骤](#基本步骤)
            * [例子详解](#例子详解)
         * [同步词库](#同步词库)
         * [其它](#其它)
      * [构建](#构建)
      * [写在最后](#写在最后)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


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

## 开始

rime 是跨平台的，在以下四个平台可用：

- **linux** 可以使用 fcitx、fxitx5、ibus

- **windows** 使用小狼毫

- **macOS** 可以用鼠须管

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



#### 安装:four_leaf_clover:四叶草输入方案

在 archlinux 下，可以从 [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 直接安装即可：

```shell
yay -S rime-cloverpinyin
```

在其它发行版下，来发布页 https://github.com/fkxxyz/rime-cloverpinyin/releases 或 https://fkxxyz.lanzous.com/b00zl958j 下载最新版本的配置文件，如 clover.schema-1.1.0.zip

然后将其解压到 ~/.config/fcitx/rime

#### 切换到:four_leaf_clover:四叶草输入方案

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

下面以 win7 为例截图示范。

#### 下载安装小狼毫

来 [rime下载页](https://rime.im/download/) 下载最新版本的小狼毫（注意 Windows XP 只最高只能下载 0.12.0），然后按照提示进行安装。

> - [小狼毫 0.14.3](https://bintray.com/rime/weasel/release)〔[下载](https://dl.bintray.com/rime/weasel/weasel-0.14.3.0-installer.exe)〕〔[更新日志](https://rime.im/release/weasel/)〕〔[历史版本](https://bintray.com/rime/weasel/release)〕〔[0.9.x 版本](https://bintray.com/lotem/rime/Weasel)〕〔[测试频道](https://bintray.com/rime/weasel/testing)〕
>   适用于 Windows 7, Windows 8/8.1, Windows 10
> - [小狼毫 0.12.0](https://bintray.com/rime/weasel/release/0.12.0)〔[下载](https://dl.bintray.com/rime/weasel/weasel-0.12.0.0-installer.exe)〕
>   适用于 Windows XP SP3

如果上述官网无法访问或者访问较慢，我在蓝奏网盘也上传了一份 https://fkxxyz.lanzous.com/b00zm9j5g

#### 下载输入方案

来发布页 https://github.com/fkxxyz/rime-cloverpinyin/releases 或 https://fkxxyz.lanzous.com/b00zl958j 下载最新版本的配置文件，如 clover.schema-1.1.0.zip

切换到小狼毫输入法（默认快捷键 Ctrl+Shift，或直接从托盘图标选择）

![](https://www.fkxxyz.com/img/weasel-1.png)

然后右键托盘图标“中”，选择“用户文件夹”

![](https://www.fkxxyz.com/img/weasel-2.png)

然后将你刚刚下载的压缩包解压到这里即可，解压后的效果如下

![](https://www.fkxxyz.com/img/weasel-3.png)

#### 切换输入方案

接着找到“输入法设定”

![](https://www.fkxxyz.com/img/weasel-4.png)

在方案选单设定中找到“四叶草简体拼音”并勾选，一般你不需要其它方案了，其它选项可以全部去掉。

然后点“中”

![](https://www.fkxxyz.com/img/weasel-5.png)



#### 美观

上述点了“中”之后，会出现界面风格设定，选中你喜欢的颜色。

![](https://www.fkxxyz.com/img/weasel-6.png)

这些设定完成后，会进行自动部署，需要等待半分钟左右，就可以使用了。

更多修改小狼毫的字体、配色方案参考 [官方配置指南--小狼毫](https://github.com/rime/home/wiki/CustomizationGuide#一例定制小狼毫字体字号)

> ### 一例、定制【小狼毫】字体字号
>
> 虽与输入方案无关，也在此列出以作参考。
>
> ```
> # weasel.custom.yaml
> 
> patch:
>   "style/font_face": "明兰"  # 字体名称，从记事本等处的系统字体对话框里能看到
>   "style/font_point": 14     # 字号，只认数字的，不认「五号」、「小五」这样的
> ```
>
> ### 一例、定制【小狼毫】配色方案
>
> 注：这款配色已经在新版本的小狼毫里预设了，做练习时，你可以将文中 `starcraft` 换成自己命名的标识。
>
> ```
> # weasel.custom.yaml
> 
> patch:
>   "style/color_scheme": starcraft    # 这项用于选中下面定义的新方案
>   "preset_color_schemes/starcraft":  # 在配色方案列表里加入标识为 starcraft 的新方案
>     name: 星际我争霸／StarCraft
>     author: Contralisk <contralisk@gmail.com>, original artwork by Blizzard Entertainment
>     text_color: 0xccaa88             # 编码行文字颜色，24位色值，用十六进制书写方便些，顺序是蓝绿红0xBBGGRR
>     candidate_text_color: 0x30bb55   # 候选项文字颜色，当与文字颜色不同时指定
>     back_color: 0x000000             # 底色
>     border_color: 0x1010a0           # 边框颜色，与底色相同则为无边框的效果
>     hilited_text_color: 0xfecb96     # 高亮文字，即与当前高亮候选对应的那部份输入码
>     hilited_back_color: 0x000000     # 设定高亮文字的底色，可起到凸显高亮部份的作用
>     hilited_candidate_text_color: 0x60ffa8  # 高亮候选项的文字颜色，要醒目！
>     hilited_candidate_back_color: 0x000000  # 高亮候选项的底色，若与背景色不同就会显出光棒
> ```
>
> 效果自己看！
>
> 也可以参照这张比较直观的图：
>
> ![img](https://camo.githubusercontent.com/95ec5aa3aa10b6f5d62295a3aea8107933881ca5/687474703a2f2f692e696d6775722e636f6d2f685374793663422e706e67)
>
> 另，此处有现成的配色方案工具供用家调配：
>
> - ~~http://tieba.baidu.com/p/2491103778~~
> - 小狼毫：https://bennyyip.github.io/Rime-See-Me/
> - 鼠须管：https://gjrobert.github.io/Rime-See-Me-squirrel/

如果你无法访问上述现成的配色方案工具，本网站也克隆了一份：

小狼毫： [Rime-See-Me](https://www.fkxxyz.com/Rime-See-Me)

鼠须管： [Rime-See-Me-squirrel](https://www.fkxxyz.com/Rime-See-Me-squirrel)

修改配置文件时要格外[注意](#基本配置)

#### 候选横排

候选词默认展示是竖排的，如果你习惯于横排展示候选词，请看 [【小狼毫】外观设定](https://github.com/rime/home/wiki/CustomizationGuide#%E5%B0%8F%E7%8B%BC%E6%AF%AB%E5%A4%96%E8%A7%80%E8%A8%AD%E5%AE%9A)

> #### 【小狼毫】外观设定
>
> 上文已介绍设定字体字号、制作配色方案的方法。
>
> 使用横向候选栏、嵌入式编码行：
>
> ```
> # weasel.custom.yaml
> patch:
>   style/horizontal: true      # 候选横排
>   style/inline_preedit: true  # 内嵌编码（仅支持TSF）
>   style/display_tray_icon: true  # 显示托盘图标
> ```

只需要将   style/horizontal: true  这一行添加到 patch: 的后一行即可，注意开头有两个空格，冒号和true之间也有一个空格，不能多也不能少，如下图所示

![](https://www.fkxxyz.com/img/weasel-7.png)

然后重新部署

![](https://www.fkxxyz.com/img/weasel-8.png)

修改配置文件时要格外[注意](#基本配置)

### 关于发布页

由于 rime 处理词库的原理是提前将词库转换为二进制文件，这个过程成为部署，所以我在[发布页](https://github.com/fkxxyz/rime-cloverpinyin/releases)提供了两个压缩包，一个包含二进制文件，一个不包含二进制文件。

- **clover.schema** 不包含二进制文件，复制到新机器上之后需要重新部署。
- **clover.schema-build** 包含二进制文件目录（build目录），复制到新机器上之后重新部署的时间大量缩短。

由于国内访问 github 较慢，所以我在蓝奏云也上传了一份 https://fkxxyz.lanzous.com/b00zl958j

## 基本配置

所有配置都围绕着用户资料夹展开，参考 [Rime 中的数据文件分布及作用](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E4%B8%AD%E7%9A%84%E6%95%B8%E6%93%9A%E6%96%87%E4%BB%B6%E5%88%86%E4%BD%88%E5%8F%8A%E4%BD%9C%E7%94%A8)

修改配置文件时需要注意：

- 严格遵守 yaml 语法，缩进都是两个空格，不能用 tab 代替，否则配置是无效的
- 只能有一个 patch: 行，如有相同的项目请合并。

> ## Rime 中的数据文件分布及作用
>
> 除程序文件以外，Rime 还包括多种数据文件。 这些数据文件存在于以下位置：
>
> [共享资料夹](https://github.com/rime/home/wiki/SharedData)
>
> - 【中州韵】 `/usr/share/rime-data/`
> - 【小狼毫】 `"安装目录\data"`
> - 【鼠须管】 `"/Library/Input Methods/Squirrel.app/Contents/SharedSupport/"`
>
> [用户资料夹](https://github.com/rime/home/wiki/UserData)
>
> - 【中州韵】 `~/.config/ibus/rime/` （0.9.1 以下版本为 `~/.ibus/rime/`）
> - 【小狼毫】 `"%APPDATA%\Rime"`
> - 【鼠须管】 `~/Library/Rime/`
>
> [共享资料夹](https://github.com/rime/home/wiki/SharedData) 包含预设输入方案的源文件。 这些文件属于 Rime 所发行软件的一部份，在访问权限控制较严格的系统上对用户是只读的，因此谢绝软件版本更新以外的任何修改—— 一旦用户修改这里的文件，很可能影响后续的软件升级或在升级时丢失数据。
>
> 在「[部署](https://github.com/rime/home/wiki/CustomizationGuide#重新布署的操作方法)」操作时，将用到这里的输入方案源文件、并结合用户定制的内容来编译预设输入方案。
>
> [用户资料夹](https://github.com/rime/home/wiki/UserData) 则包含为用户准备的内容，如：
>
> - 〔全局设定〕 `default.yaml`
> - 〔发行版设定〕 `weasel.yaml`
> - 〔预设输入方案副本〕 `<方案标识>.schema.yaml`
> - ※〔安装信息〕 `installation.yaml`
> - ※〔用户状态信息〕 `user.yaml`
>
> 编译输入方案所产出的二进制文件：
>
> - 〔Rime 棱镜〕 `<方案标识>.prism.bin`
> - 〔Rime 固态词典〕 `<词典名>.table.bin`
> - 〔Rime 反查词典〕 `<词典名>.reverse.bin`
>
> 记录用户写作习惯的文件：
>
> - ※〔用户词典〕 `<词典名>.userdb/` 或 `<词典名>.userdb.kct`
> - ※〔用户词典快照〕 `<词典名>.userdb.txt`、`<词典名>.userdb.kct.snapshot` 见于同步文件夹
>
> 以及用户自己设定的：
>
> - ※〔用户对全局设定的定制信息〕 `default.custom.yaml`
> - ※〔用户对预设输入方案的定制信息〕 `<方案标识>.custom.yaml`
> - ※〔用户自制输入方案〕及配套的词典源文件
>
> 注：以上标有 ※ 号的文件，包含用户资料，您在清理文件时要注意备份！

### 候选词个数

修改用户资料夹的 default.custom.yaml ，找到 menu/page_size 字段，如果没有则创建，设置该字段的值即可。例如

```yaml
patch:
  "menu/page_size": 8
  schema_list:
    - schema: clover
```

详见 [一例、定制每页候选数](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E6%AF%8F%E9%A0%81%E5%80%99%E9%81%B8%E6%95%B8)

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

这个快捷键可以修改，详见 [一例、定制唤出方案选单的快捷键](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E5%96%9A%E5%87%BA%E6%96%B9%E6%A1%88%E9%81%B8%E5%96%AE%E7%9A%84%E5%BF%AB%E6%8D%B7%E9%8D%B5)

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

这里其实是定制方案选单的选项，reset 表示默认选中 states 的第几个选项，更多请看[一例、定制简化字输出](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E7%B0%A1%E5%8C%96%E5%AD%97%E8%BC%B8%E5%87%BA)

### 出现候选框时按 Shift 字母不会上屏

由于 rime 的中英文切换的快捷键和 fcitx 的切换输入法的快捷键都是 shift ，fcitx 的快捷键优先于 rime，所以会导致这种情况。

解决方法：右键托盘图标，配置，打开 fcitx 的配置，点全局配置，额外的激活输入法快捷键，选择禁用。点显示高级选项，在这里的激活输入法可以设置为 shift

### 删除一个自造词

有时候错误的输入了一个词语，这个错误的词语每次会出现在候选框中，看着难过，那么可以删除这个词语。

按上下键高亮选中这个词语，然后按 Ctrl+Del 或 Shift+Del即可删除该词。（鼠须管的快捷键是 Fn + Shift + Delete）

### 词序总是错乱

有时候，发现以为自己最经常打的字候选词里一定排在第一位，但是时间长了发现好像并不是这么回事，似乎自己最近打的词比使用频率最高的词排序还要靠前，这导致大量的输入错误严重降低了打字效率，后来看到这个帖子

[『技术贴』『改进版』小狼毫五笔自动造词、网盘同步](https://tieba.baidu.com/p/5085900915)

原来 rime 的排序特点就是如此，但是这会导致词序经常很乱，也无法固定首位，怎么办呢，我就这个问题向rime作者反馈，得到的[回应](https://github.com/rime/librime/issues/377#issuecomment-644682195)是，这是记忆力算法，刚开始词序可能会变化较大，长期会趋于稳定，那这么看来暂时先这样用着时间长就好了。

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

### 导入自定义词库

可以借助[深蓝词库转换](https://github.com/studyzy/imewlconverter)这个项目，导入它所能支持的所有细胞词库如搜狗拼音细胞词库等。

#### 基本步骤

首先在用户资料夹下建立 clover.dict.yaml ，内容为

```yaml
name: clover
version: "1"
sort: by_weight

import_tables:
  - clover.base
  - clover.phrase
  - THUOCL_animal
  - THUOCL_caijing
  - THUOCL_car
  - THUOCL_chengyu
  - THUOCL_diming
  - THUOCL_food
  - THUOCL_IT
  - THUOCL_law
  - THUOCL_lishimingren
  - THUOCL_medical
  - THUOCL_poem
  - sogou_new_words
```

建立了这个文件之后，会覆盖默认的词库。

关于这个文件的格式详解： [Dict.yaml 详解](https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md#dictyaml-%E8%A9%B3%E8%A7%A3)

在这里，需要说明 import_tables 导入表里的每一项。

- **clover.base**   这是单字的字库，包含所有字的拼音、字频，对应文件 clover.base.dict.yaml
- **clover.phrase**   这是词组的词库，包含所有基本词汇的拼音、词频，对应文件 clover.phrase.dict.yaml
- **THUOCL_***   这是清华大学开源词库，对应文件 THUOCL_*.dict.yaml
- **sogou_new_words**   这是每周更新的搜狗网络流行新词，对应文件 sogou_new_words.dict.yaml

然后你可以在该文件的后面，按照上述格式（两个空格一个减号一个空格），任意添加你自己创建或导入的词库，当然你也可以删除上述你不想要的词库。

需要注意以下几点：

- clover.base 是不可以删除的，否则会失去所有文字的拼音导致导入任何词库都无效。

- 导入的词库也遵循同样的格式，但是导入的词库的 import_tables 项是无效的（也就是不能嵌套）

- 导入的词库的 name 字段必须和文件名一致，后缀为 .dict.yaml

  例如文件名 “音乐词汇大全.dict.yaml” 的第一行为

  ```yaml
  name: 音乐词汇大全
  ```

  否则导入的该词库也会无效

#### 例子详解

下面以导入搜狗音乐词汇大全的细胞词库为例

首先来这里下载该细胞词库 [音乐词汇大全](https://pinyin.sogou.com/dict/detail/index/15145)

然后用深蓝词库转换为 “音乐词汇大全.txt” ，下面是不同平台的使用方法：

- Windows端

  下载地址 [imewlconverter_Windows.zip](https://github.com/studyzy/imewlconverter/releases/download/v2.8.0/imewlconverter_Windows.zip)

  打开深蓝词库转换，指定好要转换的文件、源类型为 “搜狗细胞词库scel”，目标类型为 “Rime中州韵”，点击转换，提示是否保存点“是”，保存为 “音乐词汇大全.txt”

- archlinux

  在 archlinux 下直接从 AUR 安装深蓝词库转换即可 yay -S imewlconverter-bin

  然后执行

  ```shell
  imewlconverter -i:scel 音乐词汇大全.scel -o:rime 音乐词汇大全.txt
  ```

- 其它 linux 发行版

  下载地址 [imewlconverter_Linux_Mac.tar.gz](https://github.com/studyzy/imewlconverter/releases/download/v2.8.0/imewlconverter_Linux_Mac.tar.gz) ，解压得到 ImeWlConverterCmd

  然后执行

  ```shell
  ImeWlConverterCmd -i:scel 音乐词汇大全.scel -o:rime 音乐词汇大全.txt
  ```

- macOS端自测

然后在用户资料夹下创建 “音乐词汇大全.dict.yaml”，内容为

```yaml
name: 音乐词汇大全
version: "1.0"
sort: by_weight
...
阿炳	a bing	1
阿甲文	a jia wen	1
阿拉伯风格曲	a la bo feng ge qu	1
阿勒曼舞曲	a le man wu qu	1
```

把“音乐词汇大全.txt”里面的词都追加到后面。

然后在用户资料夹下建立 clover.dict.yaml ，内容为

```yaml
name: clover
version: "1"
sort: by_weight

import_tables:
  - clover.base
  - clover.phrase
  - THUOCL_animal
  - THUOCL_caijing
  - THUOCL_car
  - THUOCL_chengyu
  - THUOCL_diming
  - THUOCL_food
  - THUOCL_IT
  - THUOCL_law
  - THUOCL_lishimingren
  - THUOCL_medical
  - THUOCL_poem
  - sogou_new_words
  - 音乐词汇大全
```

右键托盘图标，点击“重新部署”，片刻之后，打字测试看看有没有相应的词汇吧。

### 同步词库

rime 允许不同系统之间进行词库的同步。

该功能详见 [同步用户资料](https://github.com/rime/home/wiki/UserGuide#%E5%90%8C%E6%AD%A5%E7%94%A8%E6%88%B6%E8%B3%87%E6%96%99)

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

