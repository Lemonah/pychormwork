"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 22:07
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : conftest.py
# @Project : PyCharm
==============================
"""

import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from loguru import logger


@pytest.fixture(scope='function')
def get_driver():
    logger.info("{:=^50}".format('初始化浏览器'))
    chromedriver_path = Service(r'D:\Code\python\chromedriver.exe')
    driver = webdriver.Chrome(service=chromedriver_path)
    logger.info('启动浏览器成功')
    driver.implicitly_wait(time_to_wait=10)
    url = 'https://hec.teleows.com/cas/login?service=https%3A%2F%2F1d-hec.teleows.com%3A443%2Fapp%2F1d%2Fspl%2' \
        'FmobileAttendance%2Fatt_attendance_record_grid_for_me.spl&_validateRequest_=caf0cc3b-dd84-42ca-bd83' \
        '-ac62f743668c'
    try:
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        logger.info("{:=^30}".format('考勤首页打开成功'))
    except Exception as e:
        logger.error('登录出错')
        logger.exception(e)
        raise e
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)  # scope='session'跨.py调用
def task_mark():
    logger.debug("{:=^50}".format('测试任务开始'))  # 程序运行开始打印
    yield
    logger.debug("{:=^50}".format('测试任务结束'))  # 程序结束运行打印


@pytest.fixture(autouse=True)  # 默认为function,有方法调用才记录
def case_mark():
    logger.debug("{:=^50}".format('用例开始'))
    yield
    logger.debug("{:=^50}".format('用例结束'))


if __name__ == '__main__':
    get_driver()