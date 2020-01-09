#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2020/01/10
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  _service
""""""
import servicemanager
import win32api
import win32event
import win32service
import win32serviceutil


class Service(win32serviceutil.ServiceFramework):

    # Required Attributes:
    # _svc_name_ = The service name
    # _svc_display_name_ = The service display name
    # # Optional Attributes:
    # _svc_deps_ = None        # sequence of service names on which this depends
    # _exe_name_ = None        # Default to PythonService.exe
    # _exe_args_ = None        # Default to no arguments
    # _svc_description_ = None # Only exists on Windows 2000 or later, ignored on windows NT

    def __init__(self, args):
        self.log('init')
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def log(self, msg):
        servicemanager.LogInfoMsg(str(msg))

    def sleep(self, minute):
        win32api.Sleep((minute * 1000), True)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.log('start')
            self.start()
            self.log('wait')
            win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
            self.log('done')
        except BaseException as e:
            self.log('Exception : %s' % e)
            self.SvcStop()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.log('stopping')
        self.stop()
        self.log('stopped')
        win32event.SetEvent(self.stop_event)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def start(self):
        while True:
            self.run()

    def stop(self):
        pass

    def run(self):
        pass


def service(argv, service_class):
    if len(argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(service_class)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(service_class)
