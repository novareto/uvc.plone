# -*- coding: utf-8 -*-

import Acquisition
from five import grok
from zope.interface import Interface
from Products.CMFPlone.resources import add_resource_on_request
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.choice import ChoiceSchemaField
from zeam.form.ztk.interfaces import ICollectionSchemaField
from zeam.form.base.interfaces import IWidget
from zeam.form.ztk.widgets.collection import (
    ListSchemaField, ChoiceSchemaField, MultiChoiceWidgetExtractor,
    CollectionSchemaField, newCollectionWidgetFactory, MultiChoiceFieldWidget)


class PloneFieldWidget(FieldWidget, Acquisition.Explicit):
    grok.baseclass()

    @property
    def context(self):
        # Plone Zope 2 template need a context.
        return self.form.context


class PloneMultiSelectFieldWidget(MultiChoiceFieldWidget, PloneFieldWidget):
    grok.adapts(CollectionSchemaField, ChoiceSchemaField, Interface, Interface)
    grok.name('INOUT')

    def __init__(self, field, value_field, form, request):
        super(PloneMultiSelectFieldWidget, self).__init__(
            field, value_field, form, request)
        add_resource_on_request(request, 'inout')


grok.global_adapter(
    newCollectionWidgetFactory(mode='INOUT'),
    adapts=(ICollectionSchemaField, Interface, Interface),
    provides=IWidget,
    name='INOUT')


class Extractor(MultiChoiceWidgetExtractor):
    grok.adapts(ListSchemaField, ChoiceSchemaField, Interface, Interface)
