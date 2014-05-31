# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api
from DateTime import DateTime
from datetime import datetime
import logging
from ..config import XML_FILE_DIR

logger = logging.getLogger(".sitemap")


def getXml(type=str(), start=int(), end=int()):
    catalog = api.portal.get_tool(name='portal_catalog')
    brain = catalog({'portal_type':type, 'review_state':'published'}, sort_on='created')
    headString = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
                 '''
    tailString = '</urlset>'

    itemList = ''
    for i in range(start, end):
        try:
            itemList += '<url>\n  <loc>%s</loc>\n  <lastmod>%s</lastmod>\n</url>\n' % (brain[i].getURL(), str(brain[i].ModificationDate))
        except:
            break

    return '%s\n%s%s' % (headString, itemList, tailString)


class SitemapXml(BrowserView):
    def __call__(self):
        if not (hasattr(self.request, 'type') and hasattr(self.request, 'start') and hasattr(self.request, 'end') and hasattr(self.request, 'filename')):
            return '缺少參數'

        start = int(self.request['start'])
        end = int(self.request['end'])
        portal_type = self.request['type']
        filename = self.request['filename']

        xmlString = getXml(portal_type, start, end)
        with open('%s%s' % (XML_FILE_DIR, filename), 'w') as xmlFile:
            xmlFile.write(xmlString)
        logger.info('xml寫入OK')
        return 'xml寫入OK'
