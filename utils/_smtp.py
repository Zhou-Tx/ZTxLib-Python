#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2020/7/17 0017
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  _smtp.py
""""""
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class SMTP:
    def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
    ):
        self.__user = user
        smtp = smtplib.SMTP_SSL(
            host=host
        )
        smtp.connect(
            host=host,
            port=port,
        )
        smtp.login(
            user=user,
            password=password,
        )
        self.__smtp = smtp

    def send(
            self,
            subject: str,
            message: str,
            header_from: str = '',
            *header_to: dict
    ):
        """
        Send An Email
        :param subject: 邮件标题
        :param message: 邮件内容
        :param header_from: 发件人
        :param header_to: 收件人: List<dict> [{'name':'', 'addr':''}, ...]
        :return: None
        """
        print(';'.join(['%(name)s<%(addr)s>' % to for to in header_to]))
        message = MIMEText(message, 'html', 'utf8')
        message['Subject'] = Header(subject)
        message['From'] = Header(header_from)
        message['To'] = Header(';'.join(['%(name)s<%(addr)s>' % to for to in header_to]))
        self.__smtp.sendmail(
            from_addr=self.__user,
            to_addrs=[to['addr'] for to in header_to],
            msg=message.as_string(),
        )
