#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/4/10
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import sys

from setuptools import setup

from ._classifiers import classifiers
from ._install import to_install

if len(sys.argv) <= 2:
    sys.argv.append('install')

setup(
    name="ZTxLib",
    version="0.0",
    author="Zhou TianXing",
    author_email="z.t.x@foxmail.com",
    description="Zhou TianXing's Python Library",
    url="https://github.com/Zhou-Tx/ZTxLib-Python.git",
    packages=list(to_install['packages']),
    install_requires=list(to_install['install_requires']),
    python_requires='>=3.8',
    classifiers=classifiers
)
