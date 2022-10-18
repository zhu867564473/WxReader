# -*- coding: utf-8 -*-

"""
@File    : BadNotice.py
@Time    : 2022/9/30 22:12
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 错误通知
"""

from conf.Lang import LanguageKeys
from conf.Views import Views
from helper.I18n import I18n
from helper.Preferences import UserKey
from ui.view.Notice import FillType, Notice


class BadNotice(Notice):
    """错误通知"""

    def __init__(self, tips: str):
        super(BadNotice, self).__init__(
            Views.Exception,
            UserKey.Exception.WinRect,
            I18n.text(LanguageKeys.exception_name),
            tips,
            FillType.PlainText
        )
        self.center()


class NetworkBadNotice(BadNotice):
    """网络错误通知"""

    def __init__(self):
        tips = I18n.text(LanguageKeys.debug_network_error)
        super(NetworkBadNotice, self).__init__(tips)


class InjectBadNotice(BadNotice):
    """注入脚本失败通知"""

    def __init__(self, filepath: str):
        tips = I18n.text(LanguageKeys.debug_inject_script_failed).format(filepath)
        super(InjectBadNotice, self).__init__(tips)


class ReadingFinishedNotice(Notice):
    """全文完通知"""

    def __init__(self):
        super(ReadingFinishedNotice, self).__init__(
            Views.ReadingFinished,
            UserKey.ReadingFinished.WinRect,
            I18n.text(LanguageKeys.tips_notice),
            I18n.text(LanguageKeys.tips_reading_finished),
            FillType.PlainText
        )
        self.center()
