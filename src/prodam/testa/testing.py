# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import prodam.testa


class ProdamTestaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=prodam.testa)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'prodam.testa:default')


PRODAM_TESTA_FIXTURE = ProdamTestaLayer()


PRODAM_TESTA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODAM_TESTA_FIXTURE,),
    name='ProdamTestaLayer:IntegrationTesting'
)


PRODAM_TESTA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODAM_TESTA_FIXTURE,),
    name='ProdamTestaLayer:FunctionalTesting'
)


PRODAM_TESTA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PRODAM_TESTA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ProdamTestaLayer:AcceptanceTesting'
)
