from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_neighbour import ospfNeighbour
from textwrap import dedent
import pytest


ospfNeighbourParser = ospfNeighbour + stringEnd

neighbours = [
    dedent('''\
    OSPF process 0:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.168.159.134    1   Full/DR         00:00:03    10.168.131.49   vlan2
    10.168.159.135    1   Full/DR         00:00:03    10.168.131.53   vlan3
    '''),
    dedent('''\
    OSPF process 0:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.34.64.3        1   Full/DR         00:00:04    10.34.10.209    vlan2
    10.34.64.4        1   Full/DR         00:00:04    10.34.10.213    vlan3
    '''),
    dedent('''\
    OSPF process 0:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.32.64.4        1   Full/DR         00:00:03    10.32.12.129    vlan3

    OSPF process 1009:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    78.236.0.11       1   Full/ -         00:00:03    78.236.8.229    vlan2
    '''),
    dedent('''\
    OSPF process 0:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.46.192.8       1   Full/DR         00:00:03    10.46.34.49     vlan3

    OSPF process 2:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    203.246.149.152 128   Full/ -         00:00:03    203.246.148.69  vlan2
    '''),
    dedent('''\
    OSPF process 0:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.34.64.3        1   Full/DR         00:00:04    10.34.10.209    vlan2
    10.34.64.4        1   Full/DR         00:00:04    10.34.10.213    vlan3

    OSPF process 2:
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    203.246.149.152 128   Full/ -         00:00:03    203.246.148.69  vlan4
    78.236.0.11       1   Full/ -         00:00:03    78.236.8.229    vlan5
    '''),
]

def test_ospf_neighbour_parse_ok():
    for neighbour in neighbours:
        try:
            tokens = ospfNeighbourParser.parseString(neighbour)
        except ParseException:
            print "show ip ospf neighbour:\n{}".format(neighbour)
            raise
