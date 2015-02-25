from pyzebos.parsers.config.routemap import routeMap
import pytest

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
        tokens = routeMap.parseString(route_map)
