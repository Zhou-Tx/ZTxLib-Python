#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from threading import Thread

# Private, do not touch!
class _Thread_(Thread):
    def __init__(self, method, args=None):
        super().__init__()
        self.__method = method
        self.__args = args

    def run(self):
        if self.__args==None:
            self.__method()
        else:
            self.__method(self.__args)
    

class MyThread:
    def __init__(self, method) -> 'Initialize threads with a method':
        self.__method = method

    def start(self, args=None, threadCount=5) -> 'Start to run the thread method':
        self.__threadings = []
        for t in range(threadCount):
            threading = _Thread_(self.__method, args)
            threading.start()
            self.__threadings.append(threading)

    def wait(self) -> 'Waiting for the running thread method to finish':
        for t in self.__threadings:
            t.join()
