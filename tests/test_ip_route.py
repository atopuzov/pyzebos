from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.ip.route import ipRoute
import pytest


ipRouteParser = ipRoute + stringEnd

route_statements = [
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 200 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 200 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 200 tag 20',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 200',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8 tag 20',
    'ip route 1.2.3.0 255.255.255.0 8.8.8.8',
    'ip route 1.2.3.0 255.255.255.0 vlan0 200 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 vlan0 200 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 vlan0 200 tag 20',
    'ip route 1.2.3.0 255.255.255.0 vlan0 200',
    'ip route 1.2.3.0 255.255.255.0 vlan0 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 vlan0 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0 255.255.255.0 vlan0 tag 20',
    'ip route 1.2.3.0 255.255.255.0 vlan0',
    'ip route 1.2.3.0/24 8.8.8.8 200 description Route_to_somewhere',
    'ip route 1.2.3.0/24 8.8.8.8 200 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0/24 8.8.8.8 200 tag 20',
    'ip route 1.2.3.0/24 8.8.8.8 200',
    'ip route 1.2.3.0/24 8.8.8.8 description Route_to_somewhere',
    'ip route 1.2.3.0/24 8.8.8.8 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0/24 8.8.8.8 tag 20',
    'ip route 1.2.3.0/24 8.8.8.8',
    'ip route 1.2.3.0/24 vlan0 200 description Route_to_somewhere',
    'ip route 1.2.3.0/24 vlan0 200 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0/24 vlan0 200 tag 20',
    'ip route 1.2.3.0/24 vlan0 200',
    'ip route 1.2.3.0/24 vlan0 description Route_to_somewhere',
    'ip route 1.2.3.0/24 vlan0 tag 20 description Route_to_somewhere',
    'ip route 1.2.3.0/24 vlan0 tag 20',
    'ip route 1.2.3.0/24 vlan0',
]

def test_ip_route_parse_ok():
    for route_statement in route_statements:
        try:
            tokens = ipRouteParser.parseString(route_statement)
        except ParseException:
            print "ip route: {}".format(route_statement)
            raise
