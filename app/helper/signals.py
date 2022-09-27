# -*- coding: utf-8 -*-

"""
@File    : signals.py
@Time    : 2022/9/27 16:59
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 基础信号源
"""
from PyQt5.QtCore import pyqtSignal as QSignal, QObject


class Signals(QObject):
    """Qt信号"""

    # 日志
    logger_trace = QSignal(str)
    logger_debug = QSignal(str)
    logger_info = QSignal(str)
    logger_warn = QSignal(str)
    logger_error = QSignal(str)
    logger_fatal = QSignal(str)

    # 窗口
    win_closed = QSignal(str)
    win_focus_main = QSignal()

    # 多语言
    lang_changed = QSignal(str)
