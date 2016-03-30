from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class Testa(BrowserView):
    index = ViewPageTemplateFile("templates/testa.pt")
