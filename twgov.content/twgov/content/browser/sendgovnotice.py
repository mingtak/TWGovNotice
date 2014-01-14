# -*- coding: utf-8 -*-
#from bs4 import BeautifulSoup
from Products.Five.browser import BrowserView
#from ..config import GOV_NOTICE_URL
#from ..config import PCC_DOMAIN
#from ..config import TEST_STRING
#from ..config import NOTICE_KEYWORDS
from ..config import PORTAL_DIR, SITE_URL
from plone import api
#from random import randrange
#from datetime import datetime
from DateTime import DateTime
from email.mime.text import MIMEText

def writeLog(log):
    with open('/home/plone/yyyyy', 'a') as yyyyy:
        yyyyy.write(log)


#發送govnotice 給使用者
class SendGovNotice(BrowserView):
    def __call__(self):
        #找前12小時
        start = DateTime() - 1
        now = DateTime()


        catalog = api.portal.get_tool(name='portal_catalog')
        users = api.user.get_users()
        for user in users:
            if '@' in user.emailaddress and user.checkedregister is True:
                keywords = (user.keyword1,
                            user.keyword2,
                            user.keyword3,
                            user.keyword4,
                            user.keyword5,)
                htmlString = str()
                for keyword in keywords:
                    if len(keyword.split()) == 0:
                        continue
                    dateRange = {'query':(start,now), 'range': 'min:max'}
                    brains = catalog({'Title':keyword, 'created':dateRange}, sort_on='created')
                    for brain in brains:
                        if brain.noticeName not in htmlString.decode('utf-8'):
                            url = brain.getPath().replace(PORTAL_DIR, SITE_URL)
                            htmlString += '%s%s%s%s%s%s%s' % (
                                '<li><a href="',
                                url,
                                '">',
                                brain.noticeName.encode('utf-8'),
                                '</a><span>：',
                                brain.govDepartment.encode('utf-8'),
                                '</span></li>',)

                mimeBody = MIMEText('%s%s%s' % (
                    '<html><body><h2>今日最新-Play公社,政府採購報馬仔</h2><ul>',
                    htmlString,
                    '</ul></body></html>',),
                    'html', 'utf-8')

                api.portal.send_email(recipient=user.emailaddress,
                                      sender='andy@mingtak.com.tw',
                                      subject='%s%s%s' % (user.id,
                                                        '您好，Play公社-政府採購公告：',
                                                        str(DateTime()).split()[0]),
                                      body='%s' % (mimeBody.as_string()))
#                return
            else:
                continue
