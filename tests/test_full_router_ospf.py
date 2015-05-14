from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.router.ospf import routerOSPF
import os

routerOspfParser = routerOSPF + stringEnd

config_path = os.path.join(os.getcwd(), 'tests', 'configurations', 'ospf')

def test_ospf_parse_ok():
    for (dirpath, dirnames, filenames) in os.walk(config_path):
        for filename in filenames:
            config_filename = os.path.join(dirpath, filename)
            try:
                tokens = routerOspfParser.parseFile(config_filename)
            except ParseException as pe:
                print "Failed parsing file: {}".format(config_filename)
                print "Line: {} column: {} message: {}".format(pe.lineno, pe.col, pe.msg)
                print pe.line
                print " " * (pe.col - 1) + "^"
                raise AssertionError
