# -*- coding:utf-8 -*- #

# ----------------------
# PROJECT_NAME:pychormwork
# NAME:study_niuke
# DATE:2021/11/20
# PRODUCT_NAME:PyCharm
# CODER_NAME: Panzer
# ---------------------

import random
from loguru import logger


class HJ22(object):

    def test_arr(self):
        """
        生成一个0~100的随机数表来表示空瓶
        :return:
        """
        arr = []
        while True:
            data = int(random.random()*100)  # 生成一个0-100的随机数
            if len(arr) == 10:
                logger.info('arr列表长度位10，结束循环')
                break
            elif data in arr:
                logger.info('随机数data在测试数据中，跳过')
                continue
            else:
                arr.append(data)
        return arr

    def handle_arr(self, arr: list):

        for arr_num in arr:
            if arr_num == 0:
                logger.info(f'空瓶数为 ：{arr_num}, 跳过不处理')
            elif arr_num == 1:
                logger.info(f"空瓶数为 ：{arr_num}, 空瓶数量不足")
            elif arr_num == 2:
                logger.info(f"空瓶数为 ：{arr_num}, 借1，可喝{arr_num/3}瓶")
            else:
                logger.info('进入借瓶模式')
                print(self.handle_arr_num(arr_num))
                pass

    def handle_arr_num(self, arr_num):
        drink_num = arr_num//3  # 换取的数量
        null_num = arr_num % 3  # 剩余的空瓶数
        if null_num+drink_num == 1:
            logger.info(f'可以换取{drink_num}瓶，余{null_num}空瓶')
            return drink_num
        elif null_num+drink_num == 2:
            logger.info(f'借一瓶，喝{drink_num+1}，剩1个空瓶')
            return drink_num+1
        elif null_num+drink_num > 2:
            return self.handle_arr_num(drink_num+null_num)+drink_num


if __name__ == '__main__':
    test_obj = HJ22()
    print(test_obj.test_arr())
    test_obj.handle_arr(test_obj.test_arr())