#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2019/9/21
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  MyHTML
""""""
from bs4 import BeautifulSoup
from w3lib.html import remove_tags
from urllib.parse import urlparse
import requests
import socket


class MyHTML:
    def __init__(self, url: str):
        self.__url = url
        self.__host = self._host()
        self.__ip = self._ip()
        self.__response = self._response()
        self.__beautifulSoup = self._beautiful_soup()
        self.__html = str(self.__beautifulSoup)
        self.__text = self._text()
        
    def __str__(self):
        return "<MyHTML object with url='%s'>" % self.__url

    def _host(self):
        return urlparse(self.__url).hostname

    def _ip(self):
        try:
            return socket.gethostbyname(self.__host)
        except:
            return None

    def _response(self):
        header = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                }
        try:
            return requests.get(self.__url, headers=header, timeout=30)
        except:
            return None
    
    def _beautiful_soup(self):
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
        try:
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(type(e), e)
            return None

    def _text(self):
        if self.__html == 'None':
            self.__html = None
        bs = self.__beautifulSoup
        html = self.__html
        try:
            for tags in ['script', 'style']:
                for tag in bs.find_all(tags):
                    html = html.replace(str(tag), '')
            html = ' '.join(remove_tags(html).split())
            return html
        except Exception as e:
            print(type(e), e)
            return None
    
    @property
    def URL(self):
        return self.__url

    @property
    def Host(self):
        return self.__host

    @property
    def IP(self):
        return self.__ip
    
    @property
    def Response(self):
        return self.__response

    @property
    def BeautifulSoup(self):
        return self.__beautifulSoup

    @property
    def HTML(self):
        return self.__html
    
    @property
    def Text(self):
        return self.__text
