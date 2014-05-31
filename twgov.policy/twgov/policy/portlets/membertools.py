from zope.interface import Interface
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from twgov.policy import MessageFactory as _

#from zope.i18nmessageid import MessageFactory
#__ = MessageFactory("plone")


class IMemberTools(IPortletDataProvider):

    emailErrorList = schema.Text(
        title = _(u'Email Error List'),
        required = False,
    )


class Assignment(base.Assignment):

    implements(IMemberTools)

    def __init__(self, emailErrorList=''):
        self.emailErrorList = emailErrorList
        pass

    @property
    def title(self):
        return _(u"Member tools portlet")


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('membertools.pt')

    @property
    def emailErrorList(self):
        return self.data.emailErrorList


class AddForm(base.AddForm):

    form_fields = form.Fields(IMemberTools)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):

    form_fields = form.Fields(IMemberTools)
