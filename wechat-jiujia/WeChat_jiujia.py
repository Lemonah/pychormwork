"""
=============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/12 19:14
# @Author : PANZER
# @Email : 453989453@163.com
# @File : WeChat_jiujia.py
=============================
"""

import requests
from loguru import logger
import random

# header = {
#         'Accept-Encoding': 'gzip, deflate, br',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.'
#                       '143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
#         'Cookie': '',
#         'content-type': 'application/json',
#         'Referer': r'https://servicewechat.com/wx2c7f0f3c30d99445/91/page-frame.html',
#         'zftsl': 'd3accad166a5f980ddba414c92206325',  # 这是一个随机字符串
#         'Connection': 'keep-alive',
#         'Host': 'cloud.cn2030.com'
# }


def random_str():
    """
    生成一个32位的字符串用于进入知苗的请求
    :return:
    """
    ran_str = ''
    mode_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(32):
        ran_str += mode_str[random.randint(0, len(mode_str)-1)]
    logger.info('ran_str= '+ran_str)
    return ran_str


def connect_wechat():
    """
    模拟微信vpn请求
    :return:
    """
    url = ''
    header = {}



def connect_zm():
    """
    知苗请求
    :return:
    """
    header = {
        "Accept-Encoding": "gzip, deflate, br",
        "User - Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Cookie": '',
        "content - type": "application / json",
        "Referer": "https: // servicewechat.com / wx2c7f0f3c30d99445 / 91 / page - frame.html",
        "zftsl": "f6fbe0042bc11cd35755f0d1068402fe",
        "Connection": "keep - alive",
        "Host": "cloud.cn2030.com",
    }
    params = {"act": "GetCat1"}
    url = 'cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx'
    res_mode = requests.Session()
    res = res_mode.get(url=url, headers=header, params=params)
    logger.info(f'res='+res)
    print(res.json())


if __name__ == '__main__':
    random_str()

