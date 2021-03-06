"""
============================
Author:古一
Time:2020/10/28
E-mail:369799130@qq.com
============================
整合其它几个
"""
import os

import allure
import requests
from loguru import logger

from common.handle_assert import HandleAssert
from common.handle_path import CONF_DIR
from common.utils import Utils


class BaseApi:
    conf_path = os.path.join(CONF_DIR, 'config.yaml')
    # 配置文件数据
    conf_data = Utils().handle_yaml(conf_path)  # 获取config.yaml中的数据
    host = conf_data['env']['host']  # 返回一个json格式的数据，通过jsonpath获取想要的数据，获取接口主地址
    headers = conf_data['request_headers']['headers']  # 获取请求头
    account = conf_data['account']  # 获取登录账号和密码
    investor_account = conf_data['investor_account']  # 投资账户密码
    mysql_conf = conf_data['mysql']  # 获取连接数据库的参数

    def send_http(self, data: dict):
        """
        请求封装，只负责请求，不用管数据处理，这里的数据由Utils模块处理
        发送http请求
        :param data: 请求数据
        :return: 接口返回数据response
        """
        try:
            self.__api_log(**data)
            response = requests.request(**data)
            logger.info(f"响应结果为：{response.status_code}")
        except Exception as e:
            logger.error(f'发送请求失败，请求参数为：{data}')
            logger.exception(f'发生的错误为：{e}')
            raise e
        else:
            return response

    @staticmethod  # 静态方法不强制要求传递参数
    def get_yaml(file_name):
        """
        读取yaml文件
        :param file_name: 文件路径名称
        :return: dict
        静态方法可以通过实例化调用BaseApi.get_yaml()，
        也可以不是实例化调用
        bobj = BaseApi()
        bobj.get_yaml
        """
        return Utils.handle_yaml(file_name)

    @staticmethod
    def get_token(response):
        """
        处理并提取token
        :param response:
        :return:
        """
        return Utils.handle_token(response)

    @staticmethod
    @allure.step('step:数据替换')
    def template(source_data: str, data: dict):
        """
        替换数据
        :param source_data: 源数据
        :param data: 替换内容，如{data:new_data}
        :return:
        """

        return Utils.handle_template(source_data, data)

    @staticmethod
    def to_two_decimal(data):
        """
        构造数据
        将整数或浮点数转化为两位数decimal
        :param data:
        :return:
        """
        return Utils.handle_decimal(data)

    @staticmethod
    def random_phone():
        """
        生成随机手机号
        :return:
        """
        return Utils.handle_random_phone()

    @staticmethod
    def __api_log(method, url, headers=None, params=None, json=None):
        logger.info(f"请求方式：{method}")
        logger.info(f"请求地址：{url}")
        logger.info(f"请求头：{headers}")
        logger.info(f"请求参数：{params}")
        logger.info(f"请求体：{json}")

    @staticmethod
    def assert_equal(ex, re):
        """
        断言相等
        :param ex:预期结果
        :param re:实际结果
        :return:
        """
        return HandleAssert.eq(ex, re)

    @staticmethod
    def assert_contains(content, target):
        """
        断言包含
        :param content: 文本内容
        :param target: 目标文本
        :return:
        """
        return HandleAssert.contains(content, target)


if __name__ == '__main__':
    a = BaseApi()
    a.template()
