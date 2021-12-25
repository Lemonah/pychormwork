"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 23:08
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : login_page_operation.py
# @Project : PyCharm
==============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from PY.Attendance_query_pytest.page_element import page_element
from loguru import logger


class login_page_operation():

    def __init__(self, driver, userdata):
        self.driver = driver
        self.userdata = userdata
        logger.info('userdata={}'.format(self.userdata[0]))

    def click_js_tabon(self):
        try:
            logger.info('点击邮箱和手机按钮')
            self.driver.find_element(By.ID, page_element().js_tabon).click()
        except Exception as e:
            logger.error('定位js_tabon异常')
            logger.exception(e)
            raise e

    def user_operation(self):
        try:
            user_frame = self.driver.find_element(By.ID, page_element().user_name)
            user_frame.click()
            user_frame.send_keys(self.userdata[0])
            password_frame = self.driver.find_element(By.ID, page_element().password)
            password_frame.click()
            password_frame.send_keys(self.userdata[1])
            login_button = self.driver.find_element(By.CLASS_NAME, page_element().login_button).click()
        except Exception as e:
            logger.error('用户或密码操作异常')
            logger.exception(e)
            raise e
        finally:
            return self.driver