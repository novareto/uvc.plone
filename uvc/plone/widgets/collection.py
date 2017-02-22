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


from zope.interface import Interface, implements
from zope import schema
from five.grok import GlobalUtility, name, context
from uvc.api import api
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory


class ITest(Interface):

    schlagwoerter = schema.List(
        title = u"TEST",
        required=True,
        value_type=schema.Choice(vocabulary='TEST'),
        )


class P(GlobalUtility):
    implements(IVocabularyFactory)
    name(u'TEST')

    def __call__(self, context):
        return SimpleVocabulary((SimpleTerm(title='test1', value=1),SimpleTerm(title='test2', value=2),SimpleTerm(title='test3', value=3),))

 

class TestClass(api.Form):
    context(Interface)
    fields = api.Fields(ITest)
    fields['schlagwoerter'].mode = 'INOUT'

    @api.action(u'Start')
    def action_add(self, **kw):
        data, errors = self.extractData()
        import pdb; pdb.set_trace()
