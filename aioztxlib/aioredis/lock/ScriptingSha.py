#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from . import lua_scripts

__initialized = False
ACQUIRE: str
RELEASE: str
EXTEND: str
RENEW: str


async def initialize(script_load):
    global __initialized
    if __initialized:
        return

    global ACQUIRE
    global RELEASE
    global EXTEND
    global RENEW
    ACQUIRE = await script_load(lua_scripts.ACQUIRE)
    RELEASE = await script_load(lua_scripts.RELEASE_SCRIPT)
    EXTEND = await script_load(lua_scripts.EXTEND_SCRIPT)
    RENEW = await script_load(lua_scripts.RENEW_SCRIPT)

    __initialized = True
