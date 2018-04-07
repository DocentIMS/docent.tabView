# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from docent.tabView.interfaces import ITabView
from docent.tabView.testing import DOCENT_TABVIEW_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TabViewIntegrationTest(unittest.TestCase):

    layer = DOCENT_TABVIEW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='TabView')
        schema = fti.lookupSchema()
        self.assertEqual(ITabView, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='TabView')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='TabView')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITabView.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='TabView',
            id='TabView',
        )
        self.assertTrue(ITabView.providedBy(obj))
