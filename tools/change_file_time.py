"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/20 17:02
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : change_file_time.py
# @Project : PyCharm
==============================
"""
import os, time, sys, random, re, datetime, win32file, pywintypes
from loguru import logger
from tqdm import tqdm


class change_file_time():

    def __init__(self, filepath):
        self.filepath = file_path

    def get_all_file(self):
        try:
            for dirpath, dirname, filenames in os.walk(self.filepath):
                # logger.info(f'dirpath={dirpath}', )
                # logger.info(f'dirname={dirname}', )
                # logger.info(f'filenames={filenames}', )
                if filenames is not None:
                    # 准备改时间，取出日期备用
                    pbar = tqdm(filenames)
                    for filename in pbar:
                        # logger.info(f'filename = {filename}')
                        file_date_list = re.findall(r'[(](.*?)[)]', filename)
                        # logger.debug(f'file_date = {file_date_list}')
                        # 1判断如果文件名中没有时间就造一个日期
                        if len(file_date_list) == 0 or len(file_date_list[0]) < 7:
                            file_date = self.set_year(dirpath)
                        else:
                            # 1.1取出文件名中的日期
                            file_date = file_date_list[0]
                            pass
                        # logger.info(f'最后使用的日期为file_date = {file_date}')
                        # 2.获取随机创建时间
                        create_time = self.set_creation_time()
                        # 3.获取随机修改时间
                        change_time = self.set_change_time()
                        # 4.组装时间
                        create_date, change_date = self.assemble_date(file_date, create_time, change_time)
                        # 5.将时间格式化
                        final_creat_date = self.set_time_format(create_date)
                        final_change_date = self.set_time_format(change_date)
                        # 6.修改文件时间
                        # os.utime(os.path.join(dirpath, filename), (final_creat_date, final_change_date))
                        # change_file_path = os.path.join(dirpath, filename)
                        # win32file.CreateFile(change_file_path,  win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, 0)
                        # win32file.SetFileTime(修改文件路径，create_time,access_time,modify_Times)
                        # win32file.SetFileTime(change_file_path, final_creat_date, final_change_date, final_change_date)
                        self.modify_file_times(dirpath, filename, final_creat_date, final_change_date)
                        # logger.info(f'<{filename}>时间修改成功')
                        # time.sleep(0.5)
                        pbar.set_description("Processing %s" % filename)
                else:
                    logger.debug(f'当前路径下未发现文件:{dirpath}')
        except Exception as e:
            logger.error(f'时间修改异常：{e}')
            raise e

    def set_creation_time(self):
        """
        获取创建时间
        :return:
        """
        hour = random.randint(9, 11)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        creat_time = f'{hour}:{minute}:{second}'
        return creat_time

    def set_change_time(self):
        """
        获取修改时间，最后访问时间
        :return:
        """
        hour = random.randint(18, 19)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        change_time = f'{hour}:{minute}:{second}'
        return change_time

    def get_file_date(self, file_name):
        """
        获取文件名中的日期
        :param file_name:
        :return:
        """
        try:
            file_date = re.findall(r'[(](.*?)[)]', file_name)
        except Exception as e:
            logger.error('提取文件时间异常')
            raise e
        return file_date

    def get_dirpath_month(self, dirpath):
        """
        获取文件路径中的月份数
        :return:
        """
        dirpath_date = re.findall(r'\d{2}', dirpath)
        return dirpath_date[0]

    def set_time_format(self, change_time):
        """
        格式化时间
        :return:
        """
        try:
            format = "%Y-%m-%d %H:%M:%S"
            m_time = time.mktime(time.strptime(change_time, format))
            return m_time
        except Exception as e:
            logger.error(f'格式化时间异常：{e}')
            raise e

    def set_year(self, dirpath):
        """
        当文件没有年月日，造一个
        :param dirpath:
        :return:
        """
        try:
            month = self.get_dirpath_month(dirpath)
            year = datetime.datetime.now().year
            if month in ['1', '3', '5', '7', '8', '9', '10', '12']:  # 大月
                day = random.randint(1, 31)
            elif month == '2':
                day = random.randint(1, 28)
            else:
                day = random.randint(1, 30)
            make_date = f'{year}-{month}-{day}'
        except Exception as e:
            logger.error(f'制造的年月为：{make_date}')
        return make_date

    def assemble_date(self, file_date, creat_time, change_time):
        creat_date = f'{file_date} {creat_time}'
        change_date = f'{file_date} {change_time}'
        # logger.info(f'组装后的时间-->creat_date = {creat_date}, change_date = {change_date}')
        return creat_date, change_date

    def modify_file_times(self, dirpath, filename, final_create_date, final_change_date):
        try:
            change_file_path = os.path.join(dirpath, filename)
            fh = win32file.CreateFile(change_file_path, win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None,
                                 win32file.OPEN_EXISTING, 0, 0)
            # 将时间转为一下格式
            # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=30, tm_hour=10, tm_min=32, tm_sec=42,
            # tm_wday=5, tm_yday=303, tm_isdst=0)
            c_time = time.localtime(final_create_date)
            a_time = time.localtime(final_change_date)
            # 将格式化时间转为以下格式
            # 2021-10-30 10:32:42
            create_times = pywintypes.Time(time.mktime(c_time))
            access_times = pywintypes.Time(time.mktime(a_time))
            modify_times = pywintypes.Time(time.mktime(a_time))
            win32file.SetFileTime(fh, create_times, access_times, modify_times)
        except Exception as e:
            logger.error(f'修改文件异常：{e}')
            raise e


if __name__ == '__main__':
    file_path = r'C:\Users\Administrator\Desktop\工单'
    change_file_time(file_path).get_all_file()
