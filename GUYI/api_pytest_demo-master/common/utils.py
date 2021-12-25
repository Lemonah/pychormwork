"""
============================
Author:古一
Time:2020/10/28
E-mail:369799130@qq.com
============================
数据处理
"""
from decimal import Decimal
from string import Template
from faker import Faker

import yaml
from jsonpath import jsonpath
from loguru import logger


class Utils:
    @classmethod  # 导入模块后 classname.functionname()实现调用
    def handle_yaml(cls, file_name):  # 使用classmethod注释的方法，第一个参数必须是cls
        """
        读取yaml文件
        :param file_name:
        :return:
        """
        try:
            yaml_data = yaml.safe_load(open(file_name, encoding='utf-8'))
        except Exception as e:
            logger.error(f'yaml文件读取失败，文件名称：{file_name}')
            raise e
        else:
            return yaml_data

    @classmethod
    def handle_token(cls, response):
        """
        组装token
        :param response:
        :return: 组装好的token
        """
        # 首先根据返回的数据格式进行相应的格式转换--》 response.json()
        # 再通过相应的提取方法取到相应的数据--》jsonpath(json格式的响应数据，'$..key')
        # 根据需要的格式组装token--> f'{token_type} {token_value}'
        token_type = jsonpath(response.json(), '$..token_type')[0]
        token_value = jsonpath(response.json(), '$..token')[0]
        token = f'{token_type} {token_value}'
        return token

    @classmethod
    def handle_template(cls, source_data, replace_data: dict, ):
        """
        替换文本变量
        :param source_data:来自于yaml文件
        :param replace_data: 接口返回数据
        :return:
        # 首先将需要替换的数据转为字符串--》str(source_data)
        # 再对字符串进行初始化--》Template(str(source_data))
        # 使用安全替换--》safe_substitute(**replace_data)
        # 最后将字符串再转为json格式 --》yaml.safe_load(res)
        注意 ：
        Template（str） --> 参数必须是个字符串
        safe_substitute(**replace_data)--》 **用于解包json数据避免读取错误
        替换规则：
        ‘there $a and ${b}s' -- > {'a': xxx, 'b': yyy}
        --> there xxx and yyys
        安全替换 有就替换，没有则保留原有字符
        通过匹配相同的key，将字符串中的key，替换为safe_substitute（**json）中json中key的值
        """
        res = Template(str(source_data)).safe_substitute(**replace_data)
        return yaml.safe_load(res)

    @classmethod
    def handle_decimal(cls, data: int):
        """
        将小数或整数转换为两位数decimal--》十进制
        :param data:
        :return:
        float-->转换位浮点数

        """
        x = '{0:.2f}'.format(float(data))
        return Decimal(x)

    @classmethod
    def handle_random_phone(cls):
        """
        生成随机手机号
        :return:
        """
        fake = Faker(locale='zh_CN')
        phone_number = fake.phone_number()
        return phone_number


if __name__ == '__main__':
    a = Utils.handle_random_phone()
    print(a)
