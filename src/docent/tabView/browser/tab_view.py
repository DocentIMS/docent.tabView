# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView

import logging
logger = logging.getLogger("Plone")

class TabView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request


    def __call__(self):
        return self.render()

    def render(self):
        import pdb;pdb.set_trace()
        print fin