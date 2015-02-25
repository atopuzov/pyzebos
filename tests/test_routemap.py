from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.routemap import routeMap
import pytest


routeMapParser = routeMap + stringEnd
route_map_prolouge = 'route-map RouteMapName permit 10'

def test_route_map_match_parse_ok():
    match_statements = [
        'match as-path as-path-access-list',
        'match community 10',
        'match community 10 exact-match',
        'match community 100',
        'match community 100 exact-match',
        'match community community-list',
        'match community community-list exact-match',
        'match extcommunity 10',
        'match extcommunity 10 exact-match',
        'match extcommunity 100',
        'match extcommunity 100 exact-match',
        'match extcommunity community-list',
        'match extcommunity community-list exact-match',
        'match interface lo0',
        'match ip address 10',
        'match ip address 1300',
        'match ip address access-list',
        'match ip address prefix-list prefix-list-name',
        'match ip next-hop 100',
        'match ip next-hop 1300',
        'match ip next-hop access-list-name',
        'match ip next-hop prefix-list prefix-list-name',
        'match ip peer 100',
        'match ip peer 1300',
        'match ip peer access-list-name',
        'match ipv6 address ipv6-access-list-name',
        'match ipv6 address prefix-list ipv6-prefix-list-name',
        'match ipv6 next-hop ipv6-access-list-name',
        'match ipv6 next-hop ::1',
        'match ipv6 next-hop prefix-list ipv6-prefix-list-name',
        'match ipv6 peer 100',
        'match ipv6 peer 1300',
        'match ipv6 peer ip-access-list-name',
        'match metric 100',
        'match origin egp',
        'match origin igp',
        'match origin incomplete',
        'match route-type external type-1',
        'match route-type external type-2',
        'match tag 10',
    ]

    for match_statement in match_statements:
        route_map = '{}\n {}'.format(route_map_prolouge, match_statement)
        try:
            tokens = routeMapParser.parseString(route_map)
        except ParseException:
            print "Route map:\n{}".format(route_map)
            raise

def test_route_map_set_parse_ok():
    set_statements = [
        'set aggregator as 10 1.2.3.4',
        'set as-path prepend 10',
        'set as-path prepend 10 20',
        'set as-path prepend 10 20 30',
        'set as-path prepend 10 20 30 40',
        'set atomic-aggregate ',
        'set comm-list 10 delete',
        'set comm-list 100 delete',
        'set comm-list community-list-name delete',
        'set community 1234',
        'set community 1234 1234',
        'set community 1234 11:22',
        'set community 1234 additive',
        'set community 1234 internet',
        'set community 1234 internet additive',
        'set community 1234 internet local-AS',
        'set community 1234 internet local-AS additive',
        'set community 1234 internet local-AS no-advertise',
        'set community 1234 internet local-AS no-advertise additive',
        'set community 1234 internet local-AS no-advertise no-export',
        'set community 1234 internet local-AS no-advertise no-export additive',
        'set community 1234 internet 5678 internet',
        'set community 1234 internet 5678 internet local-AS',
        'set community 1234 internet 5678 internet local-AS no-advertise',
        'set community 1234 internet 5678 internet local-AS no-advertise no-export',
        'set community 1234 internet 5678 internet local-AS no-advertise no-export additive',
        'set community 1234 internet 11:22 additive',
        'set community 1234 internet 11:22 internet',
        'set community 1234 internet 11:22 internet local-AS',
        'set community 11:22',
        'set community 11:22 1234 local-AS',
        # 'set community no-export',
        # 'set community no-advertise',
        # 'set community no-export',
        # 'set community internet 11:22',
        # 'set community internet 11:22 internet',
        # 'set dampening ',
        'set dampening 10',
        'set dampening 10 100 100 100',
        'set dampening 10 100 100 100 10',
        'set extcommunity rt 11:22',
        'set extcommunity rt 11:22 33:44',
        'set extcommunity rt 11:22 33:44 55:66',
        'set extcommunity soo 11:22',
        'set extcommunity soo 11:22 33:44',
        'set extcommunity soo 11:22 33:44 55:66',
        'set ip next-hop 1.2.3.4',
        'set ipv6 next-hop ::1',
        'set ipv6 next-hop local ::1',
        'set local-preference 10',
        # 'set metric +10',
        'set metric 100',
        # 'set metric -21',
        'set metric-type external',
        'set metric-type internal',
        'set metric-type type-1',
        'set metric-type type-2',
        'set origin egp',
        'set origin igp',
        'set origin incomplete',
        'set originator-id 1.2.3.4',
        'set tag 100',
        'set weight 100',
    ]

    for set_statement in set_statements:
        route_map = '{}\n {}'.format(route_map_prolouge, set_statement)
        try:
            tokens = routeMapParser.parseString(route_map)
        except ParseException:
            print "Route map:\n{}".format(route_map)
            raise
