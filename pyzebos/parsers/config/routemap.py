# -*- coding: utf-8 -*-
# The MIT License (MIT)

# Copyright (c) 2014 Aleksandar Topuzović <aleksandar.topuzovic@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyparsing import (Group, OneOrMore, ZeroOrMore, Suppress, Optional,
                       Keyword, Literal, Word, nums, printables)
from common import (ipv4Address, ipv6Address, naturalNumber, accesslistName,
                    interfaceName, routeMapName, suppressedKeyword)

# Match operation
# +-match

#   +-as-path
#     +-WORD [match as-path WORD]
matchAsPath = Group(suppressedKeyword('as-path') +
                    accesslistName('accesslist'))('as_path')

#   +-community
#     +-<1-99> [match community (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match community (<1-99>|<100-199>|WORD) (exact-match|)]
#     +-<100-199> [match community (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match community (<1-99>|<100-199>|WORD) (exact-match|)]
#     +-WORD [match community (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match community (<1-99>|<100-199>|WORD) (exact-match|)]
matchCommunity = Group(suppressedKeyword('community') +
                       accesslistName('accesslist') +
                       Optional(Keyword('exact-match')))('community')

#   +-extcommunity
#     +-<1-99> [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]
#     +-<100-199> [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]
#     +-WORD [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]
#       +-exact-match [match extcommunity (<1-99>|<100-199>|WORD) (exact-match|)]

matchExtcommunity = Group(suppressedKeyword('extcommunity') +
                          accesslistName('accesslist') + \
                          Optional(Keyword('exact-match')))('extcomunity')

#   +-interface
#     +-IFNAME [match interface IFNAME]
matchInterface = Group(suppressedKeyword('interface') + \
                       interfaceName('interface'))('interface')

#   +-ip
#     +-address
#       +-<1-199> [match ip address (<1-199>|<1300-2699>|WORD)]
#       +-<1300-2699> [match ip address (<1-199>|<1300-2699>|WORD)]
#       +-WORD [match ip address (<1-199>|<1300-2699>|WORD)]
#       +-prefix-list
#         +-WORD [match ip address prefix-list WORD]

# match ip address [WORD|<1-199>|<1300-2699>]
# match ip address prefix-list WORD
matchIpAddressPrefixList = Group(Suppress(Keyword('ip') + \
                                          Keyword('address') + \
                                          Keyword('prefix-list')) + \
                                 Word(printables)('prefixlist'))('address_prefix')
matchIpAddress = Group(Suppress(Keyword('ip') + \
                                Keyword('address')) + \
                       Word(printables)('accesslist'))('ip_adress')

#   +-ip
#     +-next-hop
#       +-<1-199> [match ip next-hop (<1-199>|<1300-2699>|WORD)]
#       +-<1300-2699> [match ip next-hop (<1-199>|<1300-2699>|WORD)]
#       +-WORD [match ip next-hop (<1-199>|<1300-2699>|WORD)]
#       +-prefix-list
#         +-WORD [match ip next-hop prefix-list WORD]

# match ip next-hop (WORD|<1-199>|<1300-2699>|PREFIXLIST)
# match ip next-hop prefix-list WORD
matchIpNextHopPrefixList = Group(Suppress(Keyword('ip') + \
                                    Keyword('next-hop') + \
                                    Keyword('prefix-list')) + \
                                 Word(printables)('prefixlist'))('ip_next_hop')
matchIpNextHop = Group(Suppress(Keyword('ip') + \
                                Keyword('next-hop')) + \
                       accesslistName('accesslist'))('ip_next_hop')

# match ip peer <1-199>|<1300-2699>|WORD

#   +-ip
#     +-peer
#       +-<1-199> [match ip peer (<1-199>|<1300-2699>|WORD)]
#       +-<1300-2699> [match ip peer (<1-199>|<1300-2699>|WORD)]
#       +-WORD [match ip peer (<1-199>|<1300-2699>|WORD)]
matchIPPeer = Group(Suppress('ip') +
                    Group(suppressedKeyword('peer') +
                          accesslistName('accesslist'))('peer'))('ip')

#   +-ipv6
#     +-address
#       +-WORD [match ipv6 address WORD]
#       +-prefix-list
#         +-WORD [match ipv6 address prefix-list WORD]
matchIpv6AddressPrefixList = Group(Suppress(Keyword('ipv6') + \
                                            Keyword('address') + \
                                            Keyword('prefix-list')) + \
                                   Word(printables)('prefixlist'))('address')
matchIpv6Address = Group(Suppress(Keyword('ipv6') + \
                                  Keyword('address')) + \
                         accesslistName('accesslist'))('address')


#   +-ipv6
#     +-next-hop
#       +-WORD [match ipv6 next-hop (X:X::X:X|WORD)]
#       +-X:X::X:X [match ipv6 next-hop (X:X::X:X|WORD)]
#       +-prefix-list
#         +-WORD [match ipv6 next-hop prefix-list WORD]
# _TODO_: ipv6Address
matchIpv6NextHop = Group(Suppress(Keyword('ipv6') + \
                                  Keyword('next-hop')) + \
                         accesslistName('accesslist'))('next_hop')

#   +-ipv6
#     +-peer
#       +-<1-199> [match ipv6 peer (<1-199>|<1300-2699>|WORD)]
#       +-<1300-2699> [match ipv6 peer (<1-199>|<1300-2699>|WORD)]
#       +-WORD [match ipv6 peer (<1-199>|<1300-2699>|WORD)]
# _TODO_: ipv6Address
matchIpv6Peer = Group(Suppress(Keyword('ipv6') + \
                               Keyword('peer')) + \
                      Word(printables)('accesslist'))('peer')

#   +-metric
#     +-<0-4294967295> [match metric <0-4294967295>]
matchMetric = Group(suppressedKeyword('metric') +
                    naturalNumber('metric'))('metric')

# match origin (egp|igp|incomplete)
#   +-origin
#     +-egp [match origin (egp|igp|incomplete)]
#     +-igp [match origin (egp|igp|incomplete)]
#     +-incomplete [match origin (egp|igp|incomplete)]
origin = Keyword('egp') ^ \
         Keyword('igp') ^ \
         Keyword('incomplete')
matchOrigin = Group(suppressedKeyword('origin') + \
                    origin('origin'))('origin')

#   +-route-type
#     +-external
#       +-type-1 [match route-type external (type-1|type-2)]
#       +-type-2 [match route-type external (type-1|type-2)]
routeType = Keyword('type-1') ^ \
            Keyword('type-2')
matchRouteType = Group(suppressedKeyword('route-type') +
                       suppressedKeyword('external') +
                       routeType('type'))('route_type')

#   +-tag
#     +-<0-4294967295> [match tag <0-4294967295>]
matchTag = Group(suppressedKeyword('tag') +
                 naturalNumber('tag'))('tag')

matchOptions = (matchAsPath                ^
                matchCommunity             ^
                matchExtcommunity          ^
                matchInterface             ^
                matchIpAddressPrefixList   ^
                matchIpAddress             ^
                matchIpNextHopPrefixList   ^
                matchIpNextHop             ^
                matchIPPeer                ^
                matchIpv6AddressPrefixList ^
                matchIpv6Address           ^
                matchIpv6NextHop           ^
                matchIpv6Peer              ^
                matchMetric                ^
                matchOrigin                ^
                matchRouteType             ^
                matchTag)

matchToken = Group(suppressedKeyword('match') + matchOptions)('match')

# Set operation
# +-set

#   +-aggregator
#     +-as
#       +-<1-4294967295>
#         +-A.B.C.D [set aggregator as <1-4294967295> A.B.C.D]
setAggregator = Group(suppressedKeyword('aggregator') +
                      suppressedKeyword('as') +
                      naturalNumber('as') +
                      ipv4Address('ipaddress'))('aggregator')

#   +-as-path
#     +-prepend
#       +-<1-4294967295> [set as-path prepend .<1-4294967295>]
setAsPath = Group(suppressedKeyword('as-path') +
                  suppressedKeyword('prepend') +
                  OneOrMore(naturalNumber('as')))('as_path')

#   +-atomic-aggregate [set atomic-aggregate]
setAtomicAggregate = Group(Optional(Keyword('no')) +
                           Keyword('atomic-aggregate'))('atomic-aggregate')

#   +-comm-list
#     +-<1-99>
#       +-delete [set comm-list (<1-99>|<100-199>|WORD) delete]
#     +-<100-199>
#       +-delete [set comm-list (<1-99>|<100-199>|WORD) delete]
#     +-WORD
#       +-delete [set comm-list (<1-99>|<100-199>|WORD) delete]
setCommList = Group(suppressedKeyword('comm-list') +
                    accesslistName('accesslist') +
                    suppressedKeyword('delete'))('comm_list')

# set community <1-65535>|AA:NN|internet|local-AS|no-advertise|no-export](additive)
#   +-community
#     +-<1-65535> [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-AA:NN [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-internet [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-local-AS [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-no-advertise [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-no-export [set community [<1-65535>|AA:NN|internet|local-AS|no-advertise|no-export] (additive|)]
#     +-none [set community (none)]
communityNumberFormat = naturalNumber
communityAANNFormat = Group(Word(nums, max=2)('aa') +
                            Literal(':') +
                            Word(nums, max=2)('nn'))
communityNumber = (communityNumberFormat ^ communityAANNFormat)('community')
communityActions = (Keyword('internet') ^
                    Keyword('local-AS') ^
                    Keyword('no-advertise') ^
                    Keyword('no-export'))('action')
communityInfo = Group(communityNumber +
                      ZeroOrMore(communityActions))
setCommunity = Group(Suppress(Keyword('community')) +
                     OneOrMore(communityInfo) +
                     Optional(Keyword('additive')))('community')

#   +-community-additive
#     +-AA:NN [set community-additive .AA:NN]
communityAdditive = Group(suppressedKeyword('community-additive') +
                          communityAANNFormat)('community-additive')

#   +-dampening [set dampening (<1-45>|)]
#     +-<1-45> [set dampening (<1-45>|)]
#       +-<1-20000>
#         +-<1-20000>
#           +-<1-255> [set dampening <1-45> <1-20000> <1-20000> <1-255> (<1-45>|)]
#             +-<1-45> [set dampening <1-45> <1-20000> <1-20000> <1-255> (<1-45>|)]
setDampening = Group(suppressedKeyword('dampening') +
                     OneOrMore(naturalNumber('value')))('dampening')

# set extcommunity rt|soo [ASN:NN]+
#   +-extcommunity
#     +-rt
#       +-AA:NN [set extcommunity rt .AA:NN]
#     +-soo
#       +-AA:NN [set extcommunity soo .AA:NN]
extCommunityOption = (Keyword('rt') ^
                      Keyword('soo'))('type')
setExtCommunity = Group(suppressedKeyword('extcommunity') +
                        extCommunityOption('community') +
                        OneOrMore(communityAANNFormat))('extcommunity')

#   +-ip
#     +-next-hop
#       +-A.B.C.D [set ip next-hop A.B.C.D]
setIpNextHop = Group(suppressedKeyword('ip') +
                     Group(suppressedKeyword('next-hop') +
                           ipv4Address('address'))('next_hop'))('ip')

#   +-ipv6
#     +-next-hop
#       +-X:X::X:X [set ipv6 next-hop X:X::X:X]
#       +-global
#         +-X:X::X:X [set ipv6 next-hop global X:X::X:X]
#       +-local
#         +-X:X::X:X [set ipv6 next-hop local X:X::X:X]
setIpv6NextHop = Group(suppressedKeyword('ipv6') +
                       Group(suppressedKeyword('next-hop') +
                             Optional(Keyword('local') ^
                                      Keyword('global')) +
                             ipv6Address('address'))('next_hop'))('ipv6')

#   +-local-preference
#     +-<0-4294967295> [set local-preference <0-4294967295>]
setLocalPreference = Group(suppressedKeyword('local-preference') +
                           naturalNumber('preference'))('local_preference')

# set metric [<+/-metric>|<0-4294967295>]
#   +-metric
#     +-<+/-metric> [set metric (<0-4294967295>|<+/-metric>)]
#     +-<0-4294967295> [set metric (<0-4294967295>|<+/-metric>)]
setMetricRelative = (Keyword('+') ^
                     Keyword('-'))
setMetric = Group(suppressedKeyword('metric') +
                  Optional(setMetricRelative) +
                  naturalNumber('metric'))('metric')

#   +-metric-type
#     +-1 [set metric-type (1|2)]
#     +-2 [set metric-type (1|2)]
#     +-external [set metric-type (internal|external)]
#     +-internal [set metric-type (internal|external)]
#     +-type-1 [set metric-type (type-1|type-2)]
#     +-type-2 [set metric-type (type-1|type-2)]
metricTypes = (Keyword('external') ^
               Keyword('internal') ^
               Keyword('type-1') ^
               Keyword('type-2'))('metric_type')
setMetricType = Group(suppressedKeyword('metric-type') +
                      metricTypes)('metric_type')

#   +-origin
#     +-egp [set origin (egp|igp|incomplete)]
#     +-igp [set origin (egp|igp|incomplete)]
#     +-incomplete [set origin (egp|igp|incomplete)]
origins = (Keyword('egp') ^
           Keyword('igp') ^
           Keyword('incomplete'))('origin')
setOrigin = Group(suppressedKeyword('origin') + \
                  origins)('origin')

#   +-originator-id
#     +-A.B.C.D [set originator-id A.B.C.D]
setOriginatorId = Group(suppressedKeyword('originator-id') +
                        ipv4Address('originator-id'))('originator_id')

#   +-tag
#     +-<0-4294967295> [set tag <0-4294967295>]
setTag = Group(suppressedKeyword('tag') +
               naturalNumber('tag'))('stag')

# +-set
#   +-weight
#     +-<0-4294967295> [set weight <0-4294967295>]
setWeight = Group(suppressedKeyword('weight') +
                  naturalNumber('weight'))('weight')

setOptions = (setAggregator      ^
              setAsPath          ^
              setAtomicAggregate ^
              setCommList        ^
              setCommunity       ^
              setDampening       ^
              setExtCommunity    ^
              setIpNextHop       ^
              setIpv6NextHop     ^
              setLocalPreference ^
              setMetric          ^
              setMetricType      ^
              setOrigin          ^
              setOriginatorId    ^
              setTag             ^
              setWeight)

setToken = Group(suppressedKeyword('set') + setOptions)('set')

# route-map

actionToken = (Keyword('permit') ^
               Keyword('deny'))
routeMapTokens = (Group(OneOrMore(matchToken))('match') ^
                  Group(OneOrMore(setToken))('set'))

routeMap = Group(Suppress(Keyword('route-map')) + \
                 routeMapName('name') + \
                 actionToken('action') + \
                 naturalNumber('sequence') + \
                 ZeroOrMore(routeMapTokens))('route_map')
