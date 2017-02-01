# -*- coding: utf-8 -*-

from App.config import getConfiguration
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from plone import api as ploneapi
from uvc.api import api
from zeam.form.base import DictDataManager
from zope import schema
from zope.interface import Interface
from zope.interface import Interface
from zope.interface import directlyProvides
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def possibleStandorte(context):
    return SimpleVocabulary(
    [SimpleTerm(value=u'Augsburg', token='Augsburg', title=u'Augsburg'),
     SimpleTerm(value=u'Berlin', token='Berlin', title=u'Berlin'),
     SimpleTerm(value=u'Braunschweig', token='Braunschweig', title=u'Braunschweig'),
     SimpleTerm(value=u'Dresden', token='Dresden', title=u'Dresden'),
     SimpleTerm(value=u'Duesseldorf', token='Duesseldorf', title=u'Düsseldorf'),
     SimpleTerm(value=u'Hamburg', token='Hamburg', title=u'Hamburg'),
     SimpleTerm(value=u'Koeln', token='Koeln', title=u'Köln'),
     SimpleTerm(value=u'Leipzig', token='Leipzig', title=u'Leipzig'),
     SimpleTerm(value=u'Nuernberg', token='Nuernberg', title=u'Nürnberg'),
     SimpleTerm(value=u'Stuttgart', token='Stuttgart', title=u'Stuttgart'),
     SimpleTerm(value=u'Wiesbaden', token='Wiesbaden', title=u'Wiesbaden'),
     SimpleTerm(value=u'Wupptertal', token='Wuppertal', title=u'Wuppertal')]
    )
directlyProvides(possibleStandorte, IContextSourceBinder)


class IUserProfileSchema(Interface):

    standorte = schema.List(
        title=(u'Für welche Standorte möchten Sie Nachrichten '
               + u'angezeigt bekommen?'),
        value_type=schema.Choice(source=possibleStandorte),
        required=False,
    )


class UserProfileForm(api.Form):
    api.context(Interface)
    label = u"Erweitertes Benutzerprofil"
    description = (u"Geben Sie hier an, welche Informationen "
                   + u"Sie im Intranet sehen wollen.")
    fields = api.Fields(IUserProfileSchema)
    ignoreContent=False

    def update(self):
        userid = ploneapi.user.get_current().id
        #client = MongoClient(mongoserver, mongoport)
        #db = client.profiles
        #profilecollection = db.collection
        #data = profilecollection.find_one({'userid':userid})
        defaults = {}
        data = None
        data = {'standorte': [u'Augsburg']}
        if data:
            defaults['standorte'] = data.get('standorte', [])
        self.setContentData(
            DictDataManager(defaults))

    @api.action('Speichern')
    def handle_send(self):
        data, errors = self.extractData()
        print data
        if errors:
            return
        userid = ploneapi.user.get_current().id
        #data['userid'] = userid
        #client = MongoClient(mongoserver, mongoport)
        #db = client.profiles
        #profilecollection = db.collection
        #postid = profilecollection.save(data)
        messages = IStatusMessage(self.request)
        messages.add(u"Vielen Dank. Die Daten Ihres Erweiterten Benutzerprofils wurden geändert.", type=u"info")
        url = ploneapi.portal.get().absolute_url()
        return self.redirect(url)

