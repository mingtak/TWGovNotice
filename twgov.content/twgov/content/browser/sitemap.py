# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SitemapRelatedNotice(BrowserView):

    template = ViewPageTemplateFile('templates/sitemap_relatednotice.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':['twgov.content.newrelationnotice',],
                              'review_state':'published'},
                              sort_on='modified',
                              sort_order='reverse')[:50000]
        return self.template()


class SitemapGovNotice(BrowserView):

    template = ViewPageTemplateFile('templates/sitemap_govnotice.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':['twgov.content.govnotice',],
                              'review_state':'published'},
                              sort_on='modified',
                              sort_order='reverse')[:50000]
        return self.template()
