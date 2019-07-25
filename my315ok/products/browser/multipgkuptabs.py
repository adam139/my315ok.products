
from Acquisition import aq_inner
from five import grok
from plone.dexterity.interfaces import IDexterityContent
from Products.CMFCore.utils import getToolByName


class multipgview(grok.View):
    grok.context(IDexterityContent)
    grok.require('zope2.View')
    grok.name('multipgview')
