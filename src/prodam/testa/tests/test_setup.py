# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from prodam.testa.testing import PRODAM_TESTA_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that prodam.testa is properly installed."""

    layer = PRODAM_TESTA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if prodam.testa is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'prodam.testa'))

    def test_browserlayer(self):
        """Test that IProdamTestaLayer is registered."""
        from prodam.testa.interfaces import (
            IProdamTestaLayer)
        from plone.browserlayer import utils
        self.assertIn(IProdamTestaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PRODAM_TESTA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['prodam.testa'])

    def test_product_uninstalled(self):
        """Test if prodam.testa is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'prodam.testa'))
