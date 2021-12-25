# -*- coding:utf-8 -*- #

# ----------------------
# PROJECT_NAME:pychormwork
# NAME:study
# DATE:2021/9/23
# PRODUCT_NAME:PyCharm
# CODER_NAME: Panzer
# ---------------------

import hashlib, time
import base64, yaml

a = 'hello world'


def a_hashlib_function():
    # 生成token
    a_time = int(time.time())  # 时间戳
    _token = '{}{}'.format(a, a_time)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest()  # 加密后的16进制字符串
    return a_token, a_time


def b_service_check(token, timestap):
    _token = '{}{}'.format(a, timestap)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        print('a_hashlib_function合法，继续服务')
    else:
        print('a_hashlib_function非法，停止服务')

replace_one = '%'
replace_two = '$'

def ecode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')  # 转为byte
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError('data need "byte"')
    _data = base64.encodebytes(data).decode('utf-8')  # 转为字符串
    _data = _data.replace('a', replace_one).replace('2', replace_two)  # 字符替换
    return _data

def decode(data):
    if not isinstance(data, bytes):
        raise TypeError('data need "byte" or "str"')
    replace_one_b = replace_one.encode('utf-8')  # 转为byte类型
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b, b'a').replace(replace_two_b, b'2')
    return base64.decodebytes(data).decode('utf-8')

if __name__ == '__main__':

    data = 'hello world'
    e_data = ecode(data)
    print(e_data)
    print(decode(e_data.encode('utf-8')))