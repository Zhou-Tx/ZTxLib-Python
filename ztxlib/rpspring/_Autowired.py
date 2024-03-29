#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/4/17
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from ._Context import ApplicationContext


class Autowired:
    def __init__(self, bean_name_func):
        self.name = bean_name_func.__name__

    def __get__(self, obj=None, objtype=None):
        return ApplicationContext.get_bean(self.name)
    
    def __call__(self, *args, **kwargs):
        pass
