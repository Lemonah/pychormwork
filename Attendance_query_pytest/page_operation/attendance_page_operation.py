"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 23:30
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : attendance_page_operation.py
# @Project : PyCharm
==============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from PY.Attendance_query_pytest.page_element import page_element
from loguru import logger


class attendance_page_operation():

    def __init__(self, driver):
        self.driver = driver

    def check_attendace(self):
        try:
            logger.info('检查打卡情况')
            attendance_date = self.driver.find_element(By.ID, page_element().punch_date).text
            attendance_am = self.driver.find_element(By.ID, page_element().punch_time_am).text
            attendance_pm = self.driver.find_element(By.ID, page_element().punch_time_pm).text
            attendance_state = self.driver.find_element(By.ID, page_element().punch_state).text
            punch_dict = {
                '打卡日期': attendance_date,
                '首次签到时间': attendance_am,
                '最后签到时间': attendance_pm,
                '考勤状态': attendance_state
            }
        except Exception as e:
            logger.error(f'检查考勤异常:{e}')
            raise e
        else:
            return punch_dict