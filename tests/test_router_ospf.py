from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.router.ospf import routerOSPF
import pytest


routerOspfParser = routerOSPF + stringEnd

router_ospf_prolouge = 'router ospf'
area_statements = [
    'area 10 authentication',
    'area 1.2.3.4 authentication',
    'area 10 authentication message-digest',
    'area 1.2.3.4 authentication message-digest',
    'area 10 default-cost 100',
    'area 1.2.3.4 default-cost 100',
    'area 10 filter-list access access-list-name in',
    'area 1.2.3.4 filter-list access access-list-name in',
    'area 10 filter-list access access-list-name out',
    'area 1.2.3.4 filter-list access access-list-name out',
    'area 10 filter-list prefix prefix-list-name in',
    'area 1.2.3.4 filter-list prefix prefix-list-name in',
    'area 10 filter-list prefix prefix-list-name out',
    'area 1.2.3.4 filter-list prefix prefix-list-name out',
    'area 10 nssa',
    'area 10 nssa default-information-originate',
    # 'area 10 nssa default-information-originate metric 10',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1 translator-role always',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1 translator-role never',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1 translator-role candidate',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1 translator-role always no-redistribution',
    # 'area 10 nssa default-information-originate metric 10 metric-type 1 translator-role always no-redistribution no-summary',
    'area 10 nssa no-redistribution',
    'area 10 nssa no-summary',
    # 'area 10 nssa translator-role always',
    # 'area 10 nssa translator-role never',
    # 'area 10 nssa translator-role candidate',
    'area 10 nssa no-summary no-redistribution',
    'area 10 nssa no-summary no-redistribution default-information-originate',
    'area 10 nssa no-redistribution default-information-originate no-summary',
    'area 10 range 10.0.0.0/24',
    'area 10 range 10.0.0.0/24 advertise',
    'area 10 range 10.0.0.0/24 not-advertise',
    'area 10 shortcut default',
    'area 10 shortcut disable',
    'area 10 shortcut enable',
    'area 10 stub',
    'area 10 stub no-summary',
    'area 10 virtual-link 1.2.3.4',
    'area 10 virtual-link 1.2.3.4 authentication',
    # 'area 10 virtual-link 1.2.3.4 authentication-key auth-key',
    # 'area 10 virtual-link 1.2.3.4 authentication authentication-key auth-key',
    'area 10 virtual-link 1.2.3.4 dead-interval 10',
    'area 10 virtual-link 1.2.3.4 hello-interval 10',
    # 'area 10 virtual-link 1.2.3.4 message-digest-key 1 md5 auth-key1 ',
    # 'area 10 virtual-link 1.2.3.4 message-digest-key 1 md5 auth-key1 auth-key2',
    # 'area 10 virtual-link 1.2.3.4 message-digest-key 1 md5 auth-key1 auth-key2 auth-key-3',
    'area 10 virtual-link 1.2.3.4 retransmit-interval 10',
    'area 10 virtual-link 1.2.3.4 transmit-delay 10',
    'auto-cost reference-bandwidth 100',
    'compatible rfc1583',
    'default-information originate',
    'default-information originate always',
    'default-information originate metric 100',
    'default-information originate metric 100 metric-type 1',
    'default-information originate route-map route-map-name',
    'default-information originate metric 100 metric-type 1 route-map route-map-name',
    'default-information originate always metric 100 metric-type 1 route-map route-map-name',
]

def test_route_map_match_parse_ok():
    for area_statement in area_statements:
        router_ospf = '{}\n {}'.format(router_ospf_prolouge, area_statement)
        try:
            tokens = routerOspfParser.parseString(router_ospf)
        except ParseException:
            print "Router ospf:\n{}".format(router_ospf)
            raise
