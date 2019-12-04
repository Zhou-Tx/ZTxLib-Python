#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2019/10/7
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  MyThreading
""""""
from threading import Thread


# Private, do not touch!
class _Thread(Thread):
    def __init__(self, function, **kwargs):
        super().__init__()
        self.__function = function
        self.__kwargs = kwargs

    def run(self):
        self.__function(**self.__kwargs)


class MyThread:
    def __init__(self, method) -> 'Initialize threads with a method':
        self.__method = method
        self.__threads = []

    def start(self, thread_count=1, **kwargs) -> 'Start to run the thread method':
        for t in range(thread_count):
            threading = _Thread(self.__method, **kwargs)
            threading.start()
            self.__threads.append(threading)

    def wait(self) -> 'Waiting for the running thread method to finish':
        for t in self.__threads:
            t.join()
