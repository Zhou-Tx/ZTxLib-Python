#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2020/01/10
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  _html
""""""
from bs4 import BeautifulSoup
from w3lib.html import remove_tags
from urllib.parse import urlparse
import requests
import socket


class HTML:
    def __init__(self):
        self.__url = None
        self.__response = None

    def __str__(self):
        return "<MyHTML object with url='%s'>" % self.__url

    @staticmethod
    def get(url: str, **kwargs) -> object:
        obj = HTML()
        obj.__url = url
        obj.__response = obj.__get(**kwargs)
        return obj

    @staticmethod
    def post(url: str, **kwargs) -> object:
        obj = HTML()
        obj.__url = url
        obj.__response = obj.__post(**kwargs)
        return obj

    def __get(self, **kwargs):
        # header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        # }
        return requests.get(self.__url, **kwargs)

    def __post(self, **kwargs):
        return requests.post(self.__url, **kwargs)

    @property
    def url(self) -> str:
        return self.__url

    @property
    def host(self) -> str:
        return urlparse(self.__url).hostname

    @property
    def ip(self) -> str:
        return socket.gethostbyname(self.host)

    @property
    def response(self) -> object:
        return self.__response

    @property
    def bs(self) -> BeautifulSoup or None:
        response = self.__response
        if response is None:
            return None
        charset = requests.utils.get_encodings_from_content(response.text)
        if charset:
            charset = charset[0]
        else:
            charset = response.apparent_encoding
        if charset[0:2] == 'gb':
            response.encoding = 'gb18030'
        else:
            response.encoding = charset
        return BeautifulSoup(response.text, 'html.parser')

    @property
    def html(self) -> str:
        return self.bs.prettify()

    @property
    def text(self) -> str:
        bs = self.bs
        html = self.html
        for tags in ['script', 'style']:
            for tag in bs.find_all(tags):
                html = html.replace(str(tag), '')
        return ' '.join(remove_tags(html).split())
