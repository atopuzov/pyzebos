from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.router.bgp import routerBGP
import pytest


routerBgpParser = routerBGP + stringEnd

router_bgp_prolouge = 'router bgp 7657'
bgp_statements = [
    'aggregate-address 10.0.0.0/8 as-set summary-only',
    'auto-summary',
    # 'bgp aggregate-nexthop-check',
    'bgp always-compare-med',
    # 'bgp as-local-count 55',
    'bgp bestpath as-path ignore',
    'bgp bestpath compare-confed-aspath',
    'bgp bestpath compare-routerid',
    # 'bgp bestpath dont-compare-originator-id',
    # 'bgp bestpath med missing-as-worst',
    # 'bgp bestpath med remove-recv-med',
    # 'bgp bestpath med remove-send-med',
    # 'bgp bestpath dont-compare-originator-id',
    'bgp client-to-client reflection',
    'bgp cluster-id 5',
    'bgp confederation identifier 1',
    # 'bgp confederation peer 200',
    # 'bgp config-type standard',
    # 'bgp config-type zebos',
    'bgp dampening 20 800 2500 80 25',
    'bgp default ipv4-unicast',
    'bgp default local-preference 2345555',
    'bgp deterministic-med',
    'bgp router-id 1.1.2.3',
    'bgp scan-time 10',
    # 'bgp update-delay 345',
    'distance bgp 34 23 15',
    'neighbor 1.2.3.4 activate',
    'neighbor 10.10.0.3 advertisement-interval 45',
    'neighbor 10.10.0.3 allowas-in 4',
    'neighbor 10.10.0.75 attribute-unchanged as-path med',
    'neighbor 10.10.0.75 as-origination-interval 555',
    # 'neighbor 10.10.10.1 capability dynamic',
    # 'neighbor 10.10.10.50 capability graceful-restart',
    # 'neighbor 10.10.0.5 capability orf prefix-list both',
    # 'neighbor 10.10.10.1 capability route-refresh',
    'neighbor 3.3.3.3 collide-established',
    'neighbor 10.10.10.10 connection-retry-time 125',
    'neighbor 10.10.10.1 default-originate route-map myroute',
    'neighbor 1.2.3.4 description Backup router for sales',
    'neighbor 10.11.4.26 disallow-infinite-holdtime',
    'neighbor 1.2.3.4 distribute-list mylist out',
    'neighbor 10.10.0.34 dont-capability-negotiate',
    'neighbor 10.10.10.34 ebgp-multihop 5',
    'neighbor 10.10.0.34 enforce-multihop',
    # 'neighbor 10.10.0.34 fall-over bfd multihop',
    'neighbor 10.10.0.34 filter-list out in',
    # 'neighbor 10.10.0.34 local-as 12345',
    'neighbor 10.10.0.72 maximum-prefix 1244 warning-only',
    'neighbor 10.10.0.72 next-hop-self',
    'neighbor 10.10.10.10 override-capability',
    'neighbor 10.10.10.10 passive',
    # 'neighbor group1 peer-group',
    # 'neighbor 10.10.0.63 peer-group group1',
    'neighbor 10.10.10.10 port 643',
    'neighbor 10.10.10.10 prefix-list list1 in',
    'neighbor 10.10.0.73 remote-as 345',
    'neighbor 11.11.0.74 remote-as 23456',
    'neighbor 2.2.2.2 remote-as 200',
    'neighbor 10.10.0.63 remove-private-AS',
    'neighbor 3.3.3.3 restart-time 45',
    'neighbor 10.10.10.10 route-map rmap2 in',
    'neighbor 3.3.3.3 route-reflector-client',
    'neighbor 10.10.0.72 route-server-client',
    'neighbor 10.10.0.72 send-community extended',
    'neighbor 10.10.0.72 shutdown',
    'neighbor 10.10.10.10 soft-reconfiguration inbound',
    'neighbor 10.10.10.10 strict-capability-match',
    # 'neighbor 10.10.10.10 timers 60 120',
    # 'neighbor 10.10.10.10 timers connect 10',
    'neighbor 10.10.10.10 transparent-as',
    'neighbor 10.10.10.10 transparent-nexthop',
    'neighbor 10.10.0.73 unsuppress-map mymap',
    'neighbor 10.10.0.72 update-source myif',
    'neighbor 10.10.10.10 version 4',
    'neighbor 10.10.10.10 weight 60',
    'neighbor 3ffe:506::1 remote-as 7657',
    'neighbor 3ffe:506::1 interface eth1',
    'network synchronization',
    # 'network 2.0.0.0',
]

def test_bgp_parse_ok():
    for bgp_statement in bgp_statements:
        router_bgp = '{}\n {}'.format(router_bgp_prolouge, bgp_statement)
        try:
            tokens = routerBgpParser.parseString(router_bgp)
        except ParseException:
            print "Router bgp:\n{}".format(router_bgp)
            raise