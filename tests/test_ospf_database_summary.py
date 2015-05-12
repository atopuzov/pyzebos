
from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_database import routerLSA, networkLSA, summaryLSA, externalLSA


summaryLSAParser = summaryLSA + stringEnd

summary_lsas = [
    '''\
                Summary Link States (Area 0.0.0.0)

  LS age: 1611
  Options: 0x22 (-|-|DC|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.33.2.0 (summary Network Number)
  Advertising Router: 10.33.3.254
  LS Seq Number: 800048ae
  Checksum: 0xc12b
  Length: 28
  Network Mask: /23
        TOS: 0  Metric: 1

    ''',
    '''\
                Summary Link States (Area 0.0.0.0)

  LS age: 783
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.38.160.0 (summary Network Number)
  Advertising Router: 10.38.0.12
  LS Seq Number: 8000ace4
  Checksum: 0x23b7
  Length: 28
  Network Mask: /19
        TOS: 0  Metric: 4

    ''',
    '''\
                Summary Link States (Area 0.0.0.0)

  LS age: 1011
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.52.234.0 (summary Network Number)
  Advertising Router: 10.52.233.254
  LS Seq Number: 80000c78
  Checksum: 0x1f7f
  Length: 28
  Network Mask: /23
        TOS: 0  Metric: 1000

  LS age: 897
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.52.234.0 (summary Network Number)
  Advertising Router: 10.52.233.255
  LS Seq Number: 80000c6e
  Checksum: 0x2d7a
  Length: 28
  Network Mask: /23
        TOS: 0  Metric: 1000

    ''',
    '''\
                Summary Link States (Area 0.0.0.0)

  LS age: 783
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.38.160.0 (summary Network Number)
  Advertising Router: 10.38.0.12
  LS Seq Number: 8000ace4
  Checksum: 0x23b7
  Length: 28
  Network Mask: /19
        TOS: 0  Metric: 4

  LS age: 160
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.52.232.0 (summary Network Number)
  Advertising Router: 10.52.233.254
  LS Seq Number: 800022a5
  Checksum: 0x98c4
  Length: 28
  Network Mask: /23
        TOS: 0  Metric: 1000

  LS age: 590
  Options: 0x2 (-|-|-|-|-|-|E|-)
  LS Type: summary-LSA
  Link State ID: 10.52.232.0 (summary Network Number)
  Advertising Router: 10.52.233.255
  LS Seq Number: 8000228a
  Checksum: 0xc8ae
  Length: 28
  Network Mask: /23
        TOS: 0  Metric: 1000
    ''',
]

def test_summary_lsa_parse_ok():
    for lsa in summary_lsas:
        try:
            tokens = summaryLSAParser.parseString(lsa)
        except ParseException:
            print "lsa:\n{}".format(lsa)
            raise
