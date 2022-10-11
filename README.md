### 一、前言

**微读阅读器**从**2020.02.17**开始立项，出发点原本就是一个意外，但东西出来之后，意外地收到了很多朋友的喜欢和关注。

从最初的网页版，衍变到后来基于**Electron.js**开发的PC版问世，自此之后**微读阅读器**的版本就一直停留在**1.3.0**。 因为它纯粹是我一时热血上头开发的一个小工具，所以不会让它太占用我的个人时间。
尽管后来收到了一些反馈和建议，但是 U Know，懒是阶段性的，热情下头之后就很难抬起手来继续了。

如今，时隔两年半，收到了不少用户反馈之后，**微读阅读器2.0** 终于发布啦！

相比 **1.3**，**2.0** 做了比较大的改进，主要包括：

- 弃用 **Electron.js** 框架，改用 **PyQt5** 作为底层支持;
- 所有操作都放在了工具栏，操作更加简单直接，大大提升用户体验；
- 修复大范围挂机暂停的问题：
    - **1.3** 在切换页面之后就会进行滚动判定，如果内容未加载完毕，可能造成误判；**2.0** 只有当页面内容完全载入之后才会开启滚动；
    - **1.3** 的页面滚动失效问题比较严重，**2.0** 使用应用级定时器来刷新滚动状态，目前测试来看还算比较稳定；
- 优化自动阅读时暂停的条件：选中文本、打开目录、打开评论；
- 增加速度、步幅设置，放宽速度限制；
- 增加全文阅读完成时发送 **GET** 请求的功能；
- **2.0**将完全开源，但未经允许禁止投入商业使用。

最后，**微读阅读器2.0**是基于 **PyQy5** 全新开发的，整个过程差不多花了一周 _（因为国庆罢工啦）_，时间上是比较仓促的， 因此很可能还存在一些问题或体验上的不足，后续会陆续跟进维护，也欢迎大家到[官方仓库][1]提问题。

---

### 二、快捷键

|   快捷键   |   说明           |
|   ----    |   ----          |
|   F1      |   打开帮助        |
|   F2      |   打开关于        |
|   F3      |   回到首页        |
|   F5      |   刷新页面        |
|   F8      |   导出笔记        |
|   F9      |   切换主题        |
|   F10     |   自动阅读开关     |
|   F11     |   切换全屏        |
|   F12     |   更多选项        |
|   +       |   加快滚动速度     |
|   -       |   降低滚动速度     |
|   Home    |   回到顶部        |
|   End     |   滚到顶部        |
|   PgUp    |   向上滚动一个视图  |
|   PgDn    |   向下滚动一个视图  |
|   ←      |   上一章(页)       |
|   →      |   下一章(页)       |
|   ↑       |   向上滚动一行     |
|   ↓       |   向下滚动一行     |

---

### 三、常见问题

- 如果碰到开启自动阅读之后页面没有反应的情况，可以尝试刷新一下页面，基本可以解决问题；
- 如有其他问题或建议，请到[官方仓库][1]进行讨论;
- 你也可以给我发邮件 **jl88744653@gmail.com**，但请确保主题是**我为微读提意见**，不然可能会被我过滤掉。

[1]: https://github.com/DoooReyn/WxReader

[2]: https://github.com/DoooReyn/WxRead-PC-AutoReader
