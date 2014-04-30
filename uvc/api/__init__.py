import logging
logger = logging.getLogger('uvc.api')

def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)


def skip_tests_path(name):
    return name in ['tests', 'ftests', 'testing', 'uvcsite_registrations', 'plone_registrations']

from grokcore.component import zcml
zcml.skip_tests = skip_tests_path

