# -*- coding: utf-8 -*-
# @Time : 2021/2/24 16:02
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : yaml_read.py
# @Project : PyCharm

import yaml
import jsonpath
from PY.interfacepytest.tools.loging import logger


class YamlHandle:

    def yaml_read(self, file):
        """

        :param file:  yaml文件路径
        :param test_name:  需要的测试用例名称
        :return:
        """
        try:
            logger.info('开始读取yaml文件')
            with open(file, encoding='utf-8') as f:
                # 字典列表 五个场景五个字典
                value = yaml.load(f, Loader=yaml.FullLoader)
                logger.info('yaml文件读取成功，返回数据：{}'.format(value))
                return value
                # value_case = []
                # for i in value:
                #     value_dict = i.get(test_name)
                #     if value_dict is None:
                #         pass
                #     else:
                #         value_case.append(value_dict)
                # return value_case
        except Exception as e:
            logger.error('yaml文件读取错误：{}'.format(e))



if __name__ == '__main__':
    # ['常规场景测试', '无线热岛场景测试', '无线弱覆盖场景测试', '无线优覆盖场景测试', '基本场景覆盖测试']
    file = r'D:\PyCharm\PY\mobileTicket\address.yaml'
    test_name = 'test_case02'
    value = YamlHandle().yaml_read(file)

    print(value[0])
    test_data = jsonpath.jsonpath(value[0], '$..test_case01')[0]
    for i in test_data:
        print(test_data.get(i))

    #print(test_key_list)
    print(test_data)

