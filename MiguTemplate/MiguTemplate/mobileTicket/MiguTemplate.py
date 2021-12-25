# -*- coding: utf-8 -*-
# @Time : 2021/7/12 15:13
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : MiguTemplate.py
# @Project : PyCharm

import os, openpyxl,  jsonpath, yaml, time
from loguru import logger
from functools import partial
from openpyxl.styles import Border, Side, colors, Alignment


class MiguTemplate(object):

    def handle_yaml(self,):
        try:
            debug_yaml_file_path = os.path.join(os.getcwd(), 'test_data_yaml.yaml')
            yaml_file_path = os.path.join(os.getcwd(), 'mobile_address.yaml')
            # yaml_file_path = input('请输入ymal文件地址：')
            with open(yaml_file_path, encoding='utf-8') as f:
                test_data = yaml.load(f, Loader=yaml.FullLoader)
                # logger.debug(f'read yaml file value is : {test_data}')
                return test_data
        except Exception as e:
            logger.error(f'read yaml file false as {e}')

    def handle_test_data(self, test_data_all):
        # test_data_all = self.handle_yaml()
        test_data_list = []
        testname_lsit = []
        for test_data in test_data_all:
            list_len = []
            test_data_dict = jsonpath.jsonpath(test_data, '$..testdate')[0]
            testname = self.handle_testname(test_data)  # jsonpath.jsonpath(test_data, '$..name')
            # logger.debug(f'test_data_dict: {test_data_dict}')
            # logger.debug(f'testname: {testname}')
            for data in test_data_dict.values():
                for i in range(2):
                    test_data_list.append(data)
                    testname_lsit.append(testname[0])
                    list_len.append(data)
        logger.debug(f'testname_lsit：{testname_lsit}')
        logger.debug(f'测试名称列表长度={len(testname_lsit)}, 测试日期列表长度={len(test_data_list)}')
        logger.debug(f'test_data_lsit01 = {test_data_list}')
        return test_data_list, testname_lsit

    def handle_testname(self, test_data):
        # test_data = self.handle_yaml()
        testname_list = jsonpath.jsonpath(test_data, '$..name')
        # logger.debug(f'testname_dict = {testname_list} ')
        return testname_list

    def hanlde_save_file(self):
        try:
            now_time = int(time.time())
            mode_exl = os.path.join(os.getcwd(), 'test_mode/MiguTaskImplementRecordTemplate.xlsx')
            logger.info(f'模板路径为：{mode_exl}')
            work_book = openpyxl.load_workbook(mode_exl)
            work_sheet = work_book['Sheet1']
            save_file_path = os.path.join(input('请输入保存路径：'), f'MiguTaskImplementRecordTemplate{now_time}.xlsx')
            logger.debug(f'save_file_path:{save_file_path}')
            return work_book, work_sheet, save_file_path
        except Exception as e:
            logger.error(f'创建工作对象异常：{e}')

    def hanlde_tester(self, run_now):
        tester_list = ['dd_linyunzhi', 'dd_tanganfa']
        if run_now % 2 == 0:
            tester = tester_list[0]
        else:
            tester = tester_list[1]
        return tester

    def handle_exl_data(self, test_data_list, testname_lsit, run_now):
        tester = self.hanlde_tester(run_now)
        implementationContent = '四川省端到端媒体质量优化分析-' + testname_lsit[run_now]
        implementationStartDate = test_data_list[run_now] + '  9:00:00'
        implementationEndtDate = test_data_list[run_now] + '  18:00:00'
        breakStartTime = test_data_list[run_now] + '  12:00:00'
        breakEndtTime = test_data_list[run_now] + '  13:00:00'
        implementationTime = 8
        exl_data_list = [tester, implementationContent, implementationStartDate, implementationEndtDate,
                         breakStartTime, breakEndtTime, implementationTime]
        return exl_data_list
        pass

    def save_fun(self):
        test_data = self.handle_yaml()
        work_book, work_sheet, save_file_path = self.hanlde_save_file()
        test_data_list, testname_lsit = self.handle_test_data(test_data)
        for run_now in range(len(test_data_list)):
            exl_data = self.handle_exl_data(test_data_list, testname_lsit, run_now)
            work_sheet.append(exl_data)
        work_book.save(save_file_path)


if __name__ == '__main__':
    migu = MiguTemplate()
    migu.save_fun()
