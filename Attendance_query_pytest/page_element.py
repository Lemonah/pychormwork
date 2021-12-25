"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 22:23
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : page_element.py
# @Project : PyCharm
==============================
"""
import pytest
from selenium.webdriver.common.by import By


class page_element():

    def __init__(self):
        self.loginw3 = 'loginW3'
        self.js_tabon = 'js_tabon'  # 邮箱和手机登录
        self.user_name = 'uid'
        self.password = 'password'
        self.login_button = 'login_submit_pwd_v2'
        self.punch_date = 'ext-gen144'  # 打卡日期
        self.punch_time_am = 'ext-gen188'  # 首次签到时间
        self.punch_time_pm = 'ext-gen232'  # 最后签到时间
        self.punch_state = 'ext-gen254'  # 考勤状态
