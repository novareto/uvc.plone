# -*- coding: utf-8 -*-

import logging
from grokcore.component import zcml


logger = logging.getLogger('uvc.plone')


def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)


def skip_tests_path(name):
    return name in ['tests', 'ftests', 'testing',
                    'uvcsite_registrations', 'plone_registrations']


zcml.skip_tests = skip_tests_path
