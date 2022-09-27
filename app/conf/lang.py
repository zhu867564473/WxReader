# -*- coding: utf-8 -*-

"""
@File    : lang.py
@Time    : 2022/9/27 16:20
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 语言包
  - 可以根据需要配置语言包
"""

from enum import Enum, unique

ABOUT_CN = """
### Hi, there! 🤠 I'm DoooReyn.

-   🐼  A game developer from China
-   👷‍️ A repeat wheel maker
-   😘  A faithful fan of PyQt
-   🧙‍️ Currently focusing on `Cocos2d-x / Cocos Creator`


### Projects

-   📘 [微信读书自动阅读器 Web版](https://github.com/DoooReyn/WxRead-WebAutoReader) 
-   📗 [微信读书自动阅读器 PC版](https://github.com/DoooReyn/WxRead-PC-AutoReader)
-   👌 [手势识别与训练模型](https://wu57.cn/Game/gestures/)
-   🖕 [Cocos Creator 手势识别](https://github.com/DoooReyn/ccc-gesture-recognition) > [在线演示](https://wu57.cn/games/gesture/web-desktop/)
-   😎 [Cocos2d-x 目录监视器](https://github.com/DoooReyn/cocos2d-x-dir-monitor)
-   🛤️ [Cocos2d-x 内置 WebSocket 服务器](https://github.com/DoooReyn/cocos2d-x-lws)
-   💻 [Cocos2d-x 内置 HTTP 服务器](https://github.com/DoooReyn/cocos2d-x-lhs)
-   🎸 [Cocos2d-x Fmod 集成指南](https://github.com/DoooReyn/fmod-for-cocos2dx)
-   📓 [Cocos2d-x 使用 spdlog](https://github.com/DoooReyn/cocos2d-x-spdlog)
-   🌕 [Cocos2d-x 接入 lua-protobuf](https://github.com/DoooReyn/cocos2d-x-lua-protobuf)
-   🕹️ [Console for Cocos2d-x based on PyQt5](https://github.com/DoooReyn/Console)
-   🧰 [位图字体工具箱 BMFontToolbox](https://github.com/DoooReyn/BMFontToolbox)
-   💰 [给人事的工资明细助手](https://wu57.cn/Game/SalaryBook/)
-   ⚔️ [Lua 字符串插值](https://github.com/DoooReyn/lua-string-interpolate)
-   📬 [Formatted log for Lua](https://github.com/DoooReyn/lua_format_log)
-   📚 [IT 电子书收藏夹](https://github.com/DoooReyn/dbooks-links.git)
-   📒 [微信/支付宝账单转换器](https://github.com/DoooReyn/wechat-alipay-bill-converter)
-   👾 [虾虾虾鼓捣的 Web Game Demo](https://wu57.cn/Game/games/)

### Find Me

-   ✍️ [Blog](https://wu57.cn/)
-   📚 [简书](https://www.jianshu.com/u/5b3708fe7f63)
-   💌 jl88744653@gmail.com

"""

HELP_CN = """
### 帮助
"""


class _Languages:
    """
    语言包列表
    """
    CN = {
        # general
        "app:name": "微读自动阅读器",

        # main menu
        "main_menu:more": "更多",
        "main_menu:more:help": "帮助",
        "main_menu:more:about": "关于",
        "main_menu:more:profile": "选项",
        "main_menu:more:quit": "退出",

        # toolbar
        "toolbar:auto": "自动阅读",
        "toolbar:export": "导出笔记",
        "toolbar:theme": "切换主题",
        "toolbar:fullscreen": "切换全屏",
        "toolbar:back_home": "回到首页",
        "toolbar:speed_up": "加速",
        "toolbar:speed_dw": "减速",
        "toolbar:sponsor": "赞助",

        # notice
        "notice:btn_ok": "好哒！",
        "notice:about": ABOUT_CN,
        "notice:help": HELP_CN,

        # debug
        "debug:method_not_implemented": "[ {0} > {1} ] 方法未实现",

    }


@unique
class LangPack(Enum):
    """语言包可选项"""
    CN = _Languages.CN
