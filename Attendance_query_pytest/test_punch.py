"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 22:15
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : test_punch.py
# @Project : PyCharm
==============================
"""
import datetime
import time

from loguru import logger
from PY.Attendance_query_pytest.send_email import send_email
from PY.Attendance_query_pytest.page_operation.attendance_page_operation import attendance_page_operation
from PY.Attendance_query_pytest.page_operation.home_page_operation import home_page_operation
from PY.Attendance_query_pytest.page_operation.login_page_operation import login_page_operation
from PY.ATTENDANCE_QUERY.handle_excle import HandleExcle
from PY.Attendance_query_pytest.send_email import send_email
from apscheduler.schedulers.blocking import BlockingScheduler
import pytest

data = HandleExcle().read_exl()


class Testcase_punch():

    @pytest.mark.parametrize('data', data)
    def testcase01(self, data, get_driver):
        try:
            # 获取driver
            driver = get_driver
            home_driver = home_page_operation(driver).click_loginw3()
            login_driver = login_page_operation(home_driver, data)
            login_driver.click_js_tabon()
            attendance_driver = login_driver.user_operation()
            punch_dict = attendance_page_operation(attendance_driver).check_attendace()
            logger.debug(punch_dict)
            send_email(punch_dict, data).send_email()
        except Exception as e:
            logger.error('测试用例异常：{}'.format(e))
            raise e


if __name__ == '__main__':
    # pytest.main(['-s', '-v'])
    fiveDay = (datetime.datetime.now() + datetime.timedelta(days=5))
    fiveStyleDay = fiveDay.strftime('%Y-%m-%d')
    sched = BlockingScheduler()
    sched.add_job(pytest.main(['-s', '-v']), 'cron', day_of_week='mon-fri', hour=18, minute=30,
                   start_date=f"{time.strftime('%Y-%m-%d',time.localtime())}", end_date=f'{fiveStyleDay}')