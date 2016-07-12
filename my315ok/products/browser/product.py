#-*- coding: UTF-8 -*-
# from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from my315ok.products.product import Iproduct
from Products.Five.browser import BrowserView 

class view(BrowserView):
#     grok.context(Iproduct)
#     grok.require('zope2.View')
#     grok.name('view')

    @memoize
    def isImageAvalable(self,brain=None):
        """判断图片字段是否有效"""

        if brain is None:
            obj = self.context
        else:
            obj = brain.getObject()
        try:
            size = obj.image.size
        except:
            size = obj.image.getSize()                 
        return (size != 0)

        
    def transfer2text(self,obj):
        try:
            res = obj.output
            return res
        except:
            return obj
        
    @memoize
    def img_tag(self,scale=None,fieldname="image"):
        scales = getMultiAdapter((self.context, self.request), name='images')
        if scale == None:
            scale = scales.scale(fieldname, scale=scale)
        else:
            scale = scales.scale(fieldname, scale=scale)            
        imageTag = scale.tag()
        return imageTag


    def img_large_link(self,fieldname="image",large="large"):
        link = self.img_url() + "/@@images/" + fieldname + "/" + large
        return link
    
    def img_url(self):
        return self.context.absolute_url()  
            