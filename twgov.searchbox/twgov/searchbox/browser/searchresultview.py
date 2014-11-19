from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from twgov.searchbox import searchboxMessageFactory as _


class SearchResultView(BrowserView):

    template = ViewPageTemplateFile('searchresultview.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request


    def __call__(self):
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':'twgov.content.govnotice', 'SearchableText':self.request['key']},
                             sort_on='modified', sort_order='reverse')
        return self.template()
