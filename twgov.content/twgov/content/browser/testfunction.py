# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from ..config import PAGE_ACCESS_LOG_FILE
from DateTime import DateTime
import logging
from mmseg import seg_txt
from Products.CMFPlone.utils import safe_unicode
import scseg
from plone import api
import os

logger = logging.getLogger("TESTFUNCTION")

#write log data to log file
class TestFunction(BrowserView):
    def __call__(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        brains = catalog(portal_type='twgov.content.govnotice')
        count = 0
        for brain in brains:
            url = brain.getURL()
            logger.info(url)
            count += 1
            os.system('wget %s -O /tmp/testcache' % url)
            if count > 9:
                break
        return '測試完成 %s\n' % count
