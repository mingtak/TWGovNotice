# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api
from DateTime import DateTime
from datetime import datetime
import logging


logger = logging.getLogger(".sitemap")


def getAllUrl(type=str(), dateRange=int()):
    #設定時間區間
    start = DateTime() - dateRange
    now = DateTime()

    catalog = api.portal.get_tool(name='portal_catalog')

    dateRange = {'query':(start,now), 'range': 'min:max'}
    brains = catalog({'portal_type':type, 'created':dateRange}, sort_on='created')

    urlList = ''
    for brain in brains:
        urlList += '%s\n' % brain.getURL()
    return urlList


class Sitemap1(BrowserView):
    def __call__(self):
        urlList = getAllUrl(type='twgov.content.govnotice', dateRange=60)
        return urlList


class Sitemap2(BrowserView):
    def __call__(self):
        urlList = getAllUrl(type='twgov.content.relationnotice', dateRange=60)
        return urlList


class Sitemap3(BrowserView):
    def __call__(self):
        urlList = getAllUrl(type='Document', dateRange=60)
        return urlList

