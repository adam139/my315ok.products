"""refer  the plone.app.discussion catalog indexes
"""
from datetime import datetime
from my315ok.products import product as catalog
from my315ok.products.testing import MY315OK_PRODUCTS_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.indexer.delegate import DelegatingIndexerFactory
from Products.CMFCore.utils import getToolByName
from zope import event
from zope.annotation.interfaces import IAnnotations
from zope.component import createObject

import transaction
import unittest


class CatalogSetupTest(unittest.TestCase):

    layer = MY315OK_PRODUCTS_INTEGRATION_TESTING

    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))

        portal.invokeFactory(
            'my315ok.products.productfolder',
            'productfolder1')

        portal['productfolder1'].invokeFactory('my315ok.products.product', 'product1',
                                               linkurl="http://315ok.org/",
                                               text="rich text1")
        portal['productfolder1'].invokeFactory(
            'my315ok.products.product', 'product2', text="rich text2")
        portal['productfolder1'].invokeFactory(
            'my315ok.products.product', 'product3', text="rich text3")

        self.portal = portal

    def test_catalog_installed(self):
        self.assertTrue('text' in
                        self.portal.portal_catalog.indexes())
        self.assertTrue('linkurl' in
                        self.portal.portal_catalog.indexes())

    def test_conversation_total_comments(self):
        self.assertTrue(isinstance(catalog.text,
                                   DelegatingIndexerFactory))
        self.assertTrue(isinstance(catalog.linkurl,
                                   DelegatingIndexerFactory))
        p1 = self.portal['productfolder1']['product1']
        self.assertEqual(catalog.text(p1)(), "rich text1")
        self.assertEqual(catalog.linkurl(p1)(), "http://315ok.org/")

    def test_catalogsearch(self):
        catalog2 = getToolByName(self.portal, 'portal_catalog')

        results2 = list(catalog2({'text': "rich text1"}))
        self.assertEqual(len(results2), 1)
        results2 = list(catalog2({'linkurl': "http://315ok.org/"}))
        self.assertEqual(len(results2), 1)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
