# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from docent.tabView.testing import DOCENT_TABVIEW_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that docent.tabView is properly installed."""

    layer = DOCENT_TABVIEW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if docent.tabView is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'docent.tabView'))

    def test_browserlayer(self):
        """Test that IDocentTabviewLayer is registered."""
        from docent.tabView.interfaces import (
            IDocentTabviewLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocentTabviewLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DOCENT_TABVIEW_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['docent.tabView'])

    def test_product_uninstalled(self):
        """Test if docent.tabView is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'docent.tabView'))

    def test_browserlayer_removed(self):
        """Test that IDocentTabviewLayer is removed."""
        from docent.tabView.interfaces import \
            IDocentTabviewLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocentTabviewLayer, utils.registered_layers())
