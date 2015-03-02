from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.prefixlist import prefixList
import pytest


prefixListParser = prefixList + stringEnd

prefixlist_statements = [
    'ip prefix-list prefix-list-name description Descritpion of the prefix list',
    'ip prefix-list prefix-list-name seq 10 deny 10.0.0.0/24',
    'ip prefix-list prefix-list-name seq 10 deny 10.1.0.0/24 ge 26 le 28',
    'ip prefix-list prefix-list-name seq 10 deny 10.1.0.0/24 ge 26',
    'ip prefix-list prefix-list-name seq 10 deny 10.1.0.0/24 le 28',
    'ip prefix-list prefix-list-name seq 10 deny any',
    'ip prefix-list prefix-list-name seq 10 permit 10.0.0.0/24',
    'ip prefix-list prefix-list-name seq 10 permit 10.1.0.0/24 ge 26 le 28',
    'ip prefix-list prefix-list-name seq 10 permit 10.1.0.0/24 ge 26',
    'ip prefix-list prefix-list-name seq 10 permit 10.1.0.0/24 le 28',
    'ip prefix-list prefix-list-name seq 10 permit any',
]


def test_prefix_list_parse_ok():
    for prefixlist_statement in prefixlist_statements:
        try:
            tokens = prefixListParser.parseString(prefixlist_statement)
        except ParseException:
            print "prefix-list:\n{}".format(prefixlist_statement)
            raise
