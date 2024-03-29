#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/4/10
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import os

from ._packages import packages

file = os.path.join(
    os.path.dirname(__file__),
    "install.txt"
)
if not os.path.exists(file):
    raise FileNotFoundError(file)

with open(file, encoding='ascii') as f:
    modules = f.readlines()
    modules = [
        package.strip()
        for package in modules
        if package.strip() in packages.keys()
    ]
    if len(modules) == 0:
        exit(0)

to_install: dict[str, set[str]] = dict(
    packages=set.union({'ztxlib'}, *[
        packages[package].package
        for package in modules
    ]),
    install_requires=set.union(*[
        packages[package].install_requires
        for package in modules
    ])
)
