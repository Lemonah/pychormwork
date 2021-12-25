"""
==============================
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 23:50
# @Author :PANZER
# @Email : 453989453@a163.com
# @File : send_email.py
# @Project : PyCharm
==============================
"""
import smtplib
from email.mime.text import MIMEText
from loguru import logger


class send_email():

    def __init__(self, punch_dict, data):
        self.punch_dict = punch_dict
        self.add_email = data

    def send_email(self):
        """
                考勤异常时发送邮件
                :return:
                """
        logger.info('发送考勤邮件')
        mail_host = 'smtp.163.com'  # 163邮箱服务器
        mail_user = '453989453@163.com'  # 163用户名
        mail_password = 'LJPOYPSGLKTQWPBU'  # 授权码
        sender = '453989453@163.com'  # 发送方地址
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = [self.add_email[2]]
        # 设置email信息
        # 邮件内容设置
        content =f"用户：{self.add_email[0]}, \r\r\n\
                 '打卡日期': {self.punch_dict['打卡日期']},\r\r\n\
                '首次签到时间': {self.punch_dict['首次签到时间']},\r\r\n\
                '最后签到时间': {self.punch_dict['最后签到时间']},\r\r\n\
                '考勤状态': {self.punch_dict['考勤状态']} \r\r\n\
                 '注：如果签到时间后面为空，则有未打卡记录"

        message = MIMEText(content, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = '考勤情况查询结果'
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        message['To'] = receivers[0]
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)  # or 587
            # smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            # 登录到服务器
            smtpObj.login(mail_user, mail_password)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            logger.info('success')
        except smtplib.SMTPException as e:
            logger.error('error', e)
            logger.exception(e)
            raise e