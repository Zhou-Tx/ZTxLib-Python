#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2020/7/17 0017
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL


class NonReceiversError(TypeError):
    pass


class SMTP:
    def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
    ):
        """

        :param host: 发件服务器地址
        :param port: 发件服务器端口号
        :param user: 用户名（发件人地址）
        :param password: 密码
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def __enter__(self) -> 'SMTP':
        self.smtp = SMTP_SSL(host=self.host, port=self.port)
        self.smtp.login(user=self.user, password=self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.smtp.quit()

    def send(
            self,
            subject: str,
            header_from: str = '',
            header_to: str = '',
            receivers: list[str] = None,
            mime_parts: list[MIMEBase] = None
    ) -> None:
        """
        发送邮件

        :param subject: 邮件主题
        :param header_from: 发件人名称
        :param header_to: 收件人名称
        :param receivers: 收件人地址
        :param mime_parts: 邮件内容
        :return:
        """
        if not isinstance(receivers, list):
            raise NonReceiversError("unresolved receivers: [%s]" % receivers)
        if len(receivers) == 0:
            raise NonReceiversError("empty receivers: %s" % receivers)

        message = MIMEMultipart()
        message['Subject'] = Header(subject)
        message['From'] = Header(f"{header_from}<{self.user}>")
        message['To'] = Header(header_to)
        if mime_parts is not None:
            for mime_part in mime_parts:
                message.attach(mime_part)

        server.sendmail(
            from_addr=self.user,
            to_addrs=receivers,
            msg=message.as_string()
        )
