from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.accesslist import accessList
import pytest


accessListParser = accessList + stringEnd

accesslist_statements = [
    # Standard access list
    'access-list 50 deny 10.0.0.0 0.0.0.255',
    'access-list 50 deny 5.6.7.8',
    'access-list 50 deny any',
    'access-list 50 permit 1.2.3.4',
    'access-list 50 permit 10.0.0.0 0.0.0.255',
    'access-list 50 permit any',
    'access-list 50 remark Comment goes here',
    # Extended access list
    'access-list 120 deny ip 10.0.0.0 0.0.0.255 11.0.0.0 0.0.0.255',
    'access-list 120 deny ip 10.0.0.0 0.0.0.255 any',
    'access-list 120 deny ip 10.0.0.0 0.0.0.255 host 1.2.3.4',
    'access-list 120 deny ip any 10.0.0.0 0.0.0.255',
    'access-list 120 deny ip any any',
    'access-list 120 deny ip any host 1.2.3.4',
    'access-list 120 deny ip host 1.2.3.4 10.0.0.0 0.0.0.255',
    'access-list 120 deny ip host 1.2.3.4 any',
    'access-list 120 deny ip host 1.2.3.4 host 5.6.7.8',
    'access-list 120 permit ip 10.0.0.0 0.0.0.255 11.0.0.0 0.0.0.255',
    'access-list 120 permit ip 10.0.0.0 0.0.0.255 any',
    'access-list 120 permit ip 10.0.0.0 0.0.0.255 host 1.2.3.4',
    'access-list 120 permit ip any 10.0.0.0 0.0.0.255',
    'access-list 120 permit ip any any',
    'access-list 120 permit ip any host 1.2.3.4',
    'access-list 120 permit ip host 1.2.3.4 10.0.0.0 0.0.0.255',
    'access-list 120 permit ip host 1.2.3.4 any',
    'access-list 120 permit ip host 1.2.3.4 host 5.6.7.8',
    'access-list 120 remark Comment goes here',
    # Named access list
    'access-list named-list deny 11.0.0.0/24 exact-match',
    'access-list named-list deny 11.0.0.0/24',
    'access-list named-list deny any',
    'access-list named-list permit 10.0.0.0/24 exact-match',
    'access-list named-list permit 10.0.0.0/24',
    'access-list named-list permit any',
    'access-list named-list remark Comment goes here',
]

def test_access_list_parse_ok():
    for accesslist_statement in accesslist_statements:
        try:
            tokens = accessListParser.parseString(accesslist_statement)
        except ParseException:
            print "access-list:\n{}".format(accesslist_statement)
            raise

