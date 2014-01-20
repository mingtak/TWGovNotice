# -*- coding: utf-8 -*-
from five import grok
from Acquisition import aq_inner
from zope.annotation.interfaces import IAnnotatable, IAnnotations
from plone import api


class KeywordsSetting(grok.View):
    """Keywords Setting View
    """

    grok.context(IAnnotatable)
    grok.require('zope2.View')
    grok.name('keywords_setting')

    def update(self):
        userItem = api.user.get_current()
        if hasattr(self.request, 'replyto'):
            isEmailString = self.request['replyto']
            if len(isEmailString.split('@')) != 2 or len(isEmailString.split('@')[1].split('.')) == 1:
                api.portal.show_message(message=u'Email 格式錯誤!!!', request=self.request, type='error')
            else:
                if self.request.has_key('checkedregister'):
                    userItem.checkedregister = True
                else:
                    userItem.checkedregister = False
                    return
                userItem.emailaddress = self.request['replyto']
                userItem.keyword1 = self.request['keyword1']
                userItem.keyword2 = self.request['keyword2']
                userItem.keyword3 = self.request['keyword3']
                userItem.keyword4 = self.request['keyword4']
                userItem.keyword5 = self.request['keyword5']
        return
