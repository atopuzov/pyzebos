from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_database import routerLSA, networkLSA, summaryLSA, externalLSA


networkLSAParser = networkLSA + stringEnd

network_lsas = [
    '''\

                Net Link States (Area 0.0.0.0)

  LS age: 968
    Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: network-LSA
    Link State ID: 10.168.66.1 (address of Designated Router)
  Advertising Router: 10.168.95.134
  LS Seq Number: 80007349
  Checksum: 0x2e4e
  Length: 32
  Network Mask: /30
        Attached Router: 10.168.95.134
        Attached Router: 10.168.66.9
    ''',
    '''\

                Net Link States (Area 0.0.0.0)

  LS age: 1475
    Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: network-LSA
    Link State ID: 10.168.66.5 (address of Designated Router)
  Advertising Router: 10.168.95.135
  LS Seq Number: 8000734d
  Checksum: 0x0270
  Length: 32
  Network Mask: /30
        Attached Router: 10.168.95.135
        Attached Router: 10.168.66.9
    ''',
    '''\

                Net Link States (Area 0.0.0.0)

  LS age: 1723
    Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: network-LSA
    Link State ID: 10.1.118.3 (address of Designated Router)
  Advertising Router: 10.1.0.2
  LS Seq Number: 800067a8
  Checksum: 0x806c
  Length: 36
  Network Mask: /24
        Attached Router: 10.1.0.2
        Attached Router: 10.1.0.1
        Attached Router: 10.1.118.46
    ''',
    '''\

                Net Link States (Area 0.0.0.0)

  LS age: 74
    Options: 0x22 (-|-|DC|-|-|-|E|-)
  LS Type: network-LSA
    Link State ID: 10.32.8.13 (address of Designated Router)
  Advertising Router: 10.32.0.2
  LS Seq Number: 800024f7
  Checksum: 0xd87b
  Length: 32
  Network Mask: /30
        Attached Router: 10.32.0.2
        Attached Router: 10.32.8.4
    ''',
    '''\
            OSPF Router with ID (128.136.12.226) (Process ID 1009)

                Net Link States (Area 0.0.0.0)

  LS age: 168
  Options: 0x22 (-|-|DC|-|-|-|E|-)
  LS Type: network-LSA
  Link State ID: 128.136.0.143 (address of Designated Router)
  Advertising Router: 178.236.0.11
  LS Seq Number: 80004126
  Checksum: 0xddc8
  Length: 32
  Network Mask: /31
        Attached Router: 128.136.0.11
        Attached Router: 128.136.0.10
    ''',
]

def test_network_lsa_parse_ok():
    for lsa in network_lsas:
        try:
            tokens = networkLSAParser.parseString(lsa)
        except ParseException:
            print "lsa:\n{}".format(lsa)
            raise
