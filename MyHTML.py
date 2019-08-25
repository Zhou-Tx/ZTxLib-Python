#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from w3lib.html import remove_tags
from socket import gethostbyname
from urllib.parse import urlparse
import requests


class MyHTML:
    def __init__(self, url:str):
        self.__url = url
        self.__host = self._Host()
        self.__ip = self._IP()
        self.__response = self._Response()
        self.__beautifulSoup = self._BeautifulSoup()
        self.__html = str(self.__beautifulSoup)
        self.__text = self._Text()
        
    def __str__(self):
        return "<MyHTML object with url='%s'>" % self.__url

    def _Host(self):
        try:
            return urlparse(self.__url).hostname
        except:
            return None

    def _IP(self):
        try:
            return gethostbyname(self.__host)
        except:
            return None

    def _Response(self):
        header = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                }
        try:
            return requests.get(self.__url, headers=header, timeout=30)
        except:
            return None
    
    def _BeautifulSoup(self):
        response = self.__response
        charset = requests.utils.get_encodings_from_content(response.text)
        if charset:
            charset = charset[0]
        else:
            charset = response.apparent_encoding
        if charset[0:2]=='gb':
            response.encoding='gb18030'
        else:
            response.encoding = charset
        try:
            return BeautifulSoup(response.text,'html.parser')
        except:
            return None

    def _Text(self):
        if self.__html=='None':
            self.__html = None
        bsobj = self.__beautifulSoup
        html = self.__html
        try:
            for tags in ['script','style']:
                for tag in bsobj.find_all(tags):
                    html = html.replace(str(tag), '')
            html = ' '.join(remove_tags(html).split())
            return html
        except:
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
