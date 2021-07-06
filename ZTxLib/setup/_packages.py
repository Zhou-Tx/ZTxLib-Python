#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/4/10
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from typing import Dict
from typing import Set


class Package:
    def __init__(self, package: Set[str] = None, install_requires: Set[str] = None):
        self.package = set() if package is None else set(package)
        self.install_requires = set() if install_requires is None else set(install_requires)


packages: Dict[str, Package] = dict(
    mariadb=Package(
        package={'ztxlib.mariadb'},
        install_requires={'mariadb>=1.0.0'},
    ),
    rpspring=Package(
        package={'ztxlib.rpspring'}
    ),
    rpbatis=Package(
        package={'ztxlib.rpbatis'}
    ),
    smtp=Package(
        package={'ztxlib.smtp'}
    )
)
