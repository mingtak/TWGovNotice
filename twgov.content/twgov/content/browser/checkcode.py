# -*- coding: utf-8 -*-
#測試相關功能用
from bs4 import BeautifulSoup
from Products.Five.browser import BrowserView
import urllib2
from ..config import GOV_NOTICE_URL
from ..config import PCC_DOMAIN
from ..config import TEST_STRING
from ..config import NOTICE_KEYWORDS
from plone import api
from random import randrange
from datetime import datetime


class CheckCode(BrowserView):
    def __call__(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        brains = catalog(id='20140117150465070887')
        result = str()
        for brain in brains:
            item = brain.getObject()
            if hasattr(item, 'organizationCode'):
                result += '%s\t%s\n' % (brain.Title.decode('utf-8'), item.organizationCode)
        return result
        
#twgov.content.govnotice
