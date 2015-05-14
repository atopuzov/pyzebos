from pyparsing import OneOrMore, stringEnd, ParseException
from pyzebos.parsers.config.routemap import routeMap
from pyzebos.parsers.common import zebosComment
import os

routeMapParser = OneOrMore(routeMap ^ zebosComment) + stringEnd

config_path = os.path.join(os.getcwd(), 'tests', 'configurations', 'route-map')

def test_routemap_parse_ok():
    for (dirpath, dirnames, filenames) in os.walk(config_path):
        for filename in filenames:
            config_filename = os.path.join(dirpath, filename)
            try:
                tokens = routeMapParser.parseFile(config_filename)
            except ParseException as pe:
                print "Failed parsing file: {}".format(config_filename)
                print "Line: {} column: {} message: {}".format(pe.lineno, pe.col, pe.msg)
                print pe.line
                print " " * (pe.col - 1) + "^"
                raise AssertionError
