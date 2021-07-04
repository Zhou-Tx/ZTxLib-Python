#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/4/11
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
# @FileName :  _classifiers
""""""
import os

classifiers = []
file = os.path.join(
    os.path.dirname(__file__),
    "classifiers.txt"
)
if os.path.exists(file):
    with open(file, encoding='ascii') as f:
        classifiers = f.readlines()
