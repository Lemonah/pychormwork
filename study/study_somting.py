# -*- coding:utf-8 -*- #

# ----------------------
# PROJECT_NAME:pychormwork
# NAME:study_somting
# DATE:2021/11/20
# PRODUCT_NAME:PyCharm
# CODER_NAME: Panzer
# ---------------------
import time, pywintypes, sys, tqdm

def str_len():
    s = input('输入：')
    s1 = s.split(' ')
    print(len(s1))
    print(len(s1[len(s1)-1]))

def myfc():
    while True:
        try:
            a = input()
            if len(a) % 8 == 0:
                c = a
            else:
                c = a + '0' * (8 - len(a) % 8)
                print(len(c))
            for i in range(int(len(c)/8)):
                print(c[i * 8:(i + 1) * 8])
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    a = [0,1,2,3,4,5,6,7,8,9]
    pdar = tqdm.tqdm(a)
    for i in pdar:
        print(i)
        pdar.set_description("Processing %s" % i)
        time.sleep(0.5)
