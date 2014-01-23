# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from ..config import PAGE_ACCESS_LOG_FILE
from DateTime import DateTime


def writeLog(log):
    with open(PAGE_ACCESS_LOG_FILE, 'a') as logFile:
        logFile.write(log + '\n')

#write log data to log file
class WriteLog(BrowserView):
    def __call__(self):
        writeLog('%s\t%s\t%s\t%s\t%s\t%s' % (str(DateTime()),
            str(self.request.get('HTTP_X_FORWARDED_FOR', ' ')),
            str(self.request.get('AUTHENTICATED_USER', ' ')),
            str(self.request.get('HTTP_REFERER', ' ')),
            str(self.request.get('VIRTUAL_URL_PARTS', ' ')[-1]),
            str(self.request.get('HTTP_USER_AGENT', ' ')),))
