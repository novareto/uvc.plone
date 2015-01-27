# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from zope import interface
from five.grok import View, Viewlet
from five import grok
from plone.api import portal
from zope.publisher.publish import mapply
from zeam.form.plone import Form
from zeam.form.base import Fields, action
from zope.component import getMultiAdapter
from AccessControl.interfaces import IUser as IPrincipal
from grokcore.layout import Layout as BaseLayout, Page
from megrok import pagetemplate as pt
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile


grok.templatedir('templates')


class Layout(BaseLayout):
    grok.name('layout')
    grok.context(interface.Interface)


def get_principal(context, request):
    portal_state = getMultiAdapter(
        (context, request), name="plone_portal_state")
    return portal_state.member().getUser()


class View(View):
    grok.baseclass()

    def getApplication(self):
        return portal.get()


class Form(Form):
    grok.baseclass()

    def getApplication(self):
        return portal.get()


class FormTemplate(pt.PageTemplate):
    pt.view(Form)


class FormMacros(grok.View):
    grok.context(interface.Interface)


__all__ = ['Fields', 'action', 'Viewlet', 'Layout', 'Form', 'Page', 'IPrincipal', 'get_principal']
