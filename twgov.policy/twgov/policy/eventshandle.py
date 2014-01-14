# -*- coding: utf-8 -*-

from five import grok
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from plone.app.contenttypes.interfaces import INewsItem, IDocument

#設定item為排除導覽
def processObject(item):
    item.exclude_from_nav = True
    item.reindexObject(idxs=['exclude_from_nav'])


@grok.subscribe(INewsItem, IObjectAddedEvent)
def handleNewsItem(newsItem, event):
    return processObject(newsItem)


@grok.subscribe(IDocument, IObjectAddedEvent)
def handleDocument(document, event):
    return processObject(document)
