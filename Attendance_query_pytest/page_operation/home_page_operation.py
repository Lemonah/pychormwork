"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 22:48
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : home_page_operation.py
# @Project : PyCharm
==============================
"""
import pytest
from PY.Attendance_query_pytest.page_element import page_element
from selenium.webdriver.common.by import By
from loguru import logger


class home_page_operation():

    def __init__(self, driver):
        self.driver = driver

    def click_loginw3(self):
        try:
            home_driver = self.driver.find_element(By.ID, page_element().loginw3)
            home_driver.click()
        except Exception as e:
            logger.error('定位loginw3异常')
            logger.exception(e)
            raise e
        finally:
            return self.driver


