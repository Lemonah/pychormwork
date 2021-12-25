# -*- coding: utf-8 -*-
# @Time : 2021/7/20 15:08
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : Handle_all_file.py
# @Project : PyCharm  工单文件一次生成
import zipfile

from PY.MiguTemplate.mobileTicket.WorkOrder_Video import WorkOrder_Video
from PY.MiguTemplate.jb_call.jb_call import JbCall
from PY.MiguTemplate.businessIntegration.CROSS_TEST import CrossTest
from PY.MiguTemplate.businessIntegration.COMPATIBILITY_TEST import CompatibilityTest
import os


class AllFile(object):

    def all_file(self):
        # 基本呼叫
        jb = JbCall()
        jb.more_line()

        w = WorkOrder_Video()
        w.more_line()

        c1 = CrossTest()
        c1.more_thread()

        c2 = CompatibilityTest()
        c2.more_thread()

    def zip_file(self):

        source_path = input('请输入需要压缩的路径：')
        outpath = source_path + '.zip'
        with zipfile.ZipFile(outpath, mode='w') as target:
            for i in os.walk(source_path):  # 这里有三个值[[文件路径]，[文件夹名], [文件名]]
                for n in i[1]:
                    target.write("".join((i[0], '\\', n)))
            target.close()


if __name__ == '__main__':

    a = AllFile()
    a.all_file()
    # a.zip_file()



