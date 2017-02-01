# -*- coding: utf-8 -*-

from five import grok
from zope.interface import Interface
from zope.schema import List, Choice
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from .api import Form, Fields


TEST = SimpleVocabulary((
    SimpleTerm(title='test1', value='Test 1'),
    SimpleTerm(title='test2', value='Test 2'),
    SimpleTerm(title='test3', value='Test 3'),
    ))



class ITestList(Interface):

    toto = List(
        title=u"test",
        value_type=Choice(vocabulary=TEST),
        required=True)


class TestForm(Form):
    grok.context(Interface)
    grok.name('test')
    
    fields = Fields(ITestList)
    ignoreContent = True
    ignoreRequest = True

    fields['toto'].mode = 'INOUT'
