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
        #取得plone預設的帳號型態
        ploneUsers = api.user.get_users()
        #cs.auth.facebook產生的id，單獨存在acl_users.cs-facebook-users中，使用portal_membership找不出來
        #使用以下三行撈出facebook型態帳號
        acl_users = api.portal.get_tool(name='acl_users')
        cs_facebook_users = getattr(acl_users, 'cs-facebook-users', '')
        facebookUsers = cs_facebook_users.enumerateUsers()

        #結合plone型態帳號與facebook型態帳號
        users = list()
        for fbUser in facebookUsers:
            users.append(fbUser['id'])
        for ploneUser in ploneUsers:
            users.append(unicode(ploneUser.id))

        for userId in users:
            user = api.user.get(userid=userId)
            emailaddress = getattr(user, 'emailaddress', 'no email,')
            if emailaddress == '':continue
            keywords = getattr(user, 'keywords', 'no keywordsList')
            oldKeyword = '%s\n%s\n%s\n%s\n%s' % (user.keyword1, user.keyword2, user.keyword3, user.keyword4, user.keyword5)
            user.keywords = oldKeyword
            logger.info('%s\t%s\t%s\t\t%s' % (safe_unicode(user.id), safe_unicode(emailaddress), safe_unicode(keywords), safe_unicode(oldKeyword)))
