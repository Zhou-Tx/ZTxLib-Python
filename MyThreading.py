#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2019/10/7
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  MyThreading
""""""
from threading import Thread


# Private, do not touch!
class _Thread_(Thread):
    def __init__(self, method, args=None):
        super().__init__()
        self.__method = method
        self.__args = args

    def run(self):
        if self.__args is None:
            self.__method()
        else:
            self.__method(self.__args)


class MyThread:
    def __init__(self, method) -> 'Initialize threads with a method':
        self.__method = method
        self.__threadings = []

    def start(self, args=None, thread_count=1) -> 'Start to run the thread method':
        for t in range(thread_count):
            threading = _Thread_(self.__method, args)
            threading.start()
            self.__threadings.append(threading)

    def wait(self) -> 'Waiting for the running thread method to finish':
        for t in self.__threadings:
            t.join()
