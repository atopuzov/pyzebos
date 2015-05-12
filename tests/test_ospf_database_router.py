from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_database import routerLSA, networkLSA, summaryLSA, externalLSA


routerLSAParser = routerLSA + stringEnd

router_lsas = [
    '''\
                Router Link States (Area 0.0.0.0)

  LS age: 1575
  Options: 0x2 (-|-|-|-|-|-|E|-)
  Flags: 0x1 : ABR
  LS Type: router-LSA
  Link State ID: 10.32.0.10
  Advertising Router: 10.32.0.10
  LS Seq Number: 8000822f
  Checksum: 0xcc1f
  Length: 204
   Number of Links: 15

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.7
     (Link Data) Router Interface address: 10.32.4.197
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.196
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.0.10
     (Link Data) Network Mask: 255.255.255.255
      Number of TOS metrics: 0
       TOS 0 Metric: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.5
     (Link Data) Router Interface address: 10.32.4.193
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.192
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.6
     (Link Data) Router Interface address: 10.32.4.195
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.194
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.8
     (Link Data) Router Interface address: 10.32.4.199
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.198
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.11
     (Link Data) Router Interface address: 10.32.0.32
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.0.32
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.1
     (Link Data) Router Interface address: 10.32.13.1
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.33
     (Link Data) Router Interface address: 10.32.13.33
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.65
     (Link Data) Router Interface address: 10.32.13.65
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.97
     (Link Data) Router Interface address: 10.32.13.97
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    ''',
    '''\
                Router Link States (Area 0.0.0.0)

  LS age: 514
  Options: 0x2 (-|-|-|-|-|-|E|-)
  Flags: 0x3 : ABR ASBR
  LS Type: router-LSA
  Link State ID: 10.32.0.11
  Advertising Router: 10.32.0.11
  LS Seq Number: 8000accd
  Checksum: 0xc359
  Length: 204
   Number of Links: 15

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.0.11
     (Link Data) Network Mask: 255.255.255.255
      Number of TOS metrics: 0
       TOS 0 Metric: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.5
     (Link Data) Router Interface address: 10.32.4.209
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.208
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.6
     (Link Data) Router Interface address: 10.32.4.211
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.210
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.7
     (Link Data) Router Interface address: 10.32.4.213
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.212
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.8
     (Link Data) Router Interface address: 10.32.4.215
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.214
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 200

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.10
     (Link Data) Router Interface address: 10.32.0.33
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.0.32
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.17
     (Link Data) Router Interface address: 10.32.13.17
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.49
     (Link Data) Router Interface address: 10.32.13.49
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.81
     (Link Data) Router Interface address: 10.32.13.81
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.13.113
     (Link Data) Router Interface address: 10.32.13.113
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    ''',
    '''\
                Router Link States (Area 0.0.0.0)

  LS age: 800
  Options: 0x22 (-|-|DC|-|-|-|E|-)
  Flags: 0x2 : ASBR
  LS Type: router-LSA
  Link State ID: 10.32.0.1
  Advertising Router: 10.32.0.1
  LS Seq Number: 8000252f
  Checksum: 0x922c
  Length: 180
   Number of Links: 13

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.0.18
     (Link Data) Router Interface address: 10.32.0.17
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.10.113
     (Link Data) Router Interface address: 10.32.10.113
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.10.33
     (Link Data) Router Interface address: 10.32.10.33
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.9.193
     (Link Data) Router Interface address: 10.32.9.193
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.9.177
     (Link Data) Router Interface address: 10.32.9.177
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.9.41
     (Link Data) Router Interface address: 10.32.9.41
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.8.105
     (Link Data) Router Interface address: 10.32.8.105
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.32.8.9
     (Link Data) Router Interface address: 10.32.8.9
      Number of TOS metrics: 0
       TOS 0 Metric: 500

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.6
     (Link Data) Router Interface address: 10.32.4.53
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.52
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.32.0.5
     (Link Data) Router Interface address: 10.32.4.25
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.4.24
     (Link Data) Network Mask: 255.255.255.254
      Number of TOS metrics: 0
       TOS 0 Metric: 100

    Link connected to: Stub Network
     (Link ID) Network/subnet number: 10.32.0.1
     (Link Data) Network Mask: 255.255.255.255
      Number of TOS metrics: 0
       TOS 0 Metric: 1

    ''',
]

def test_router_lsa_parse_ok():
    for lsa in router_lsas:
        try:
            tokens = routerLSAParser.parseString(lsa)
        except ParseException:
            print "lsa:\n{}".format(lsa)
            raise
