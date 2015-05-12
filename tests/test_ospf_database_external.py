from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_database import routerLSA, networkLSA, summaryLSA, externalLSA


externalLSAParser = externalLSA + stringEnd

external_lsas = [
    '''\
                AS External Link States

  LS age: 147
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.4.4.11 (External Network Number)
  Advertising Router: 10.34.10.233
  LS Seq Number: 8000119a
  Checksum: 0x7fb4
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 10000
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
    '''\
                AS External Link States

  LS age: 153
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.4.4.17 (External Network Number)
  Advertising Router: 10.36.190.23
  LS Seq Number: 8001817c
  Checksum: 0x6534
  Length: 36
  Network Mask: /32
        Metric Type: 2 (Larger than any link state path)
        TOS: 0
        Metric: 20
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
    '''\
                AS External Link States

  LS age: 905
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.4.8.10 (External Network Number)
  Advertising Router: 10.34.10.217
  LS Seq Number: 800085a8
  Checksum: 0x46a5
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 25000
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
    '''\
                AS External Link States

  LS age: 1014
  Options: 0x20 (-|-|DC|-|-|-|-|-)
  LS Type: AS-external-LSA
  Link State ID: 10.32.80.0 (External Network Number)
  Advertising Router: 10.32.64.2
  LS Seq Number: 800117d8
  Checksum: 0xed0c
  Length: 36
  Network Mask: /24
        Metric Type: 1
        TOS: 0
        Metric: 100
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
    '''\
                AS External Link States

  LS age: 592
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.189.127.237 (External Network Number)
  Advertising Router: 10.34.10.201
  LS Seq Number: 800001dd
  Checksum: 0x0c2a
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 25000
        Forward Address: 0.0.0.0
        External Route Tag: 0

  LS age: 1730
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.189.127.237 (External Network Number)
  Advertising Router: 10.36.10.25
  LS Seq Number: 800001dd
  Checksum: 0x1e99
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 10000
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
    '''\
                AS External Link States

  LS age: 882
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.189.127.224 (External Network Number)
  Advertising Router: 10.34.10.201
  LS Seq Number: 80000dfa
  Checksum: 0x30e9
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 25000
        Forward Address: 0.0.0.0
        External Route Tag: 0

  LS age: 169
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.189.127.224 (External Network Number)
  Advertising Router: 10.36.10.25
  LS Seq Number: 80000dfb
  Checksum: 0x405a
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 10000
        Forward Address: 0.0.0.0
        External Route Tag: 0

  LS age: 273
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: AS-external-LSA
  Link State ID: 10.189.127.225 (External Network Number)
  Advertising Router: 10.34.10.201
  LS Seq Number: 800000bb
  Checksum: 0xcb99
  Length: 36
  Network Mask: /32
        Metric Type: 1
        TOS: 0
        Metric: 25000
        Forward Address: 0.0.0.0
        External Route Tag: 0

    ''',
]

def test_external_lsa_parse_ok():
    for lsa in external_lsas:
        try:
            tokens = externalLSAParser.parseString(lsa)
        except ParseException:
            print "lsa:\n{}".format(lsa)
            raise
