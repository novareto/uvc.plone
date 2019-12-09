# -*- coding: utf-8 -*-

from five import grok
from zope.interface import Interface
from zope.schema import List, Choice, TextLine
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from .api import Form, Fields, action


TEST = SimpleVocabulary((
    SimpleTerm(title='test1', value='Test 1'),
    SimpleTerm(title='test2', value='Test 2'),
    SimpleTerm(title='test3', value='Test 3'),
    ))



class ITestList(Interface):

    name = TextLine(
        title=u"Name",
        description="DESCRIPTION"
    )



class TestForm(Form):
    grok.context(Interface)
    grok.name('test')
    
    fields = Fields(ITestList)
    ignoreContent = True
    ignoreRequest = True

    @action(u'Speichern')
    def handle_save(self):
        data, errors = self.extractData()
        print(data)
        print(errors)

