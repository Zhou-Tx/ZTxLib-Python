#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/4
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import aioredis
from .Redis import Redis
from .RedisContextManager import RedisContextManager

ConnectionsPool = aioredis.ConnectionsPool
create_pool = aioredis.create_pool
start = RedisContextManager.start

__all__ = (
    'ConnectionsPool',
    'Redis',
    'create_pool',
    'start'
)
