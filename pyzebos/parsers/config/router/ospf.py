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
#

from pyparsing import (Group, OneOrMore, ZeroOrMore, Keyword, Optional, Word,
                       alphanums)
from ...common import (ipv4Address, ipv4Prefix, ipv4AddressNetwork,
                       suppressedKeyword, accesslistName, routeMapName,
                       interfaceName, naturalNumber)

# +-area
#   +-<0-4294967295>
areaId = (naturalNumber ^
          ipv4Address)

#     +-authentication [area (A.B.C.D|<0-4294967295>) authentication]
#       +-message-digest [area (A.B.C.D|<0-4294967295>) authentication message-digest]
areaAuthentication = Group(suppressedKeyword('authentication') +
                           Optional(Keyword('message-digest')))('authentication')

#     +-default-cost
#       +-<0-16777215> [area (A.B.C.D|<0-4294967295>) default-cost <0-16777215>]
areaDefaultCost = Group(suppressedKeyword('default-cost') +
                        naturalNumber('cost'))('default_cost')

#     +-export-list
#       +-NAME [area (A.B.C.D|<0-4294967295>) export-list NAME]
areaExportList = Group(suppressedKeyword('export-list') +
                       accesslistName)('export_list')

#     +-filter-list
#       +-access
#         +-WORD
#           +-in [area (A.B.C.D|<0-4294967295>) filter-list access WORD (in|out)]
#           +-out [area (A.B.C.D|<0-4294967295>) filter-list access WORD (in|out)]
#       +-prefix
#         +-WORD
#           +-in [area (A.B.C.D|<0-4294967295>) filter-list prefix WORD (in|out)]
#           +-out [area (A.B.C.D|<0-4294967295>) filter-list prefix WORD (in|out)]
areaFilterType = (Keyword('access') ^
                  Keyword('prefix'))
areaFilterDirection = (Keyword('in') ^
                       Keyword('out'))
areaFilter = Group(suppressedKeyword('filter-list') +
                   areaFilterType +
                   accesslistName +
                   areaFilterDirection)('filter_list')

#     +-import-list
#       +-NAME [area (A.B.C.D|<0-4294967295>) import-list NAME]
areaExportList = Group(suppressedKeyword('import-list') +
                       Word(alphanums))('import_list')

#     +-nssa [area (A.B.C.D|<0-4294967295>) nssa]
#       +-default-information-originate [area (A.B.C.D|<0-4294967295>) nssa {translator-role (candidate|never|always)
#         |no-redistribution|default-information-originate (metric <0-16777214>|metric-type <1-2>
#         |metric <0-16777214> metric-type <1-2>|metric-type <1-2> metric <0-16777214>|)|no-summary}]
#       +-no-redistribution [area (A.B.C.D|<0-4294967295>) nssa {translator-role (candidate|never|always)
#         |no-redistribution|default-information-originate (metric <0-16777214>|metric-type <1-2>
#         |metric <0-16777214> metric-type <1-2>|metric-type <1-2> metric <0-16777214>|)|no-summary}]
#       +-no-summary [area (A.B.C.D|<0-4294967295>) nssa {translator-role (candidate|never|always)|no-redistribution
#         |default-information-originate (metric <0-16777214>|metric-type <1-2>|metric <0-16777214> metric-type <1-2>
#         |metric-type <1-2> metric <0-16777214>|)|no-summary}]
#       +-translate-always [area (A.B.C.D|<0-4294967295>) nssa (translate-candidate|translate-never|translate-always)]
#       +-translate-candidate [area (A.B.C.D|<0-4294967295>) nssa (translate-candidate|translate-never|translate-always)]
#       +-translate-never [area (A.B.C.D|<0-4294967295>) nssa (translate-candidate|translate-never|translate-always)]
#       +-translator-role
nssaTranslatorRoleOptions = (Keyword('candidate') +
                             Keyword('never') +
                             Keyword('always'))
nssaTranslatorRole = (Keyword('translator-role') +
                      nssaTranslatorRoleOptions)

nssaDefaultInformationOriginateMetric = (suppressedKeyword('metric') +
                                         naturalNumber('metric'))
metricType = (Keyword('1') ^
              Keyword('2'))
nssaDefaultInformationOriginateMetricType = (suppressedKeyword('metric-type') +
                                             metricType('metric_type'))
nssaDefaultInformationOriginateOptions = (Optional(nssaDefaultInformationOriginateMetric) ^
                                         Optional(nssaDefaultInformationOriginateMetricType))
nssaDefaultInformationOriginate = (Keyword('default-information-originate') +
                                  nssaDefaultInformationOriginateOptions)
nssaOptions = (nssaTranslatorRole ^
               nssaDefaultInformationOriginate ^
               Keyword('no-redistribution') ^
               Keyword('no-summary'))
areaNssa = Group(suppressedKeyword('nssa') +
                 ZeroOrMore(nssaOptions))('nssa')

#     +-range
#       +-A.B.C.D/M [area (A.B.C.D|<0-4294967295>) range A.B.C.D/M]
#         +-advertise [area (A.B.C.D|<0-4294967295>) range A.B.C.D/M advertise]
#         +-not-advertise [area (A.B.C.D|<0-4294967295>) range A.B.C.D/M not-advertise]
#         +-substitute
#           +-A.B.C.D/M [area (A.B.C.D|<0-4294967295>) range A.B.C.D/M substitute A.B.C.D/M]
areaRangeSubstitute = (Keyword('substitute') +
                       ipv4Prefix)
areaRangeOptions = (Keyword('advertise')     ^
                    Keyword('not-advertise') ^
                    areaRangeSubstitute)
areaRange = Group(suppressedKeyword('range') +
                  ipv4Prefix('prefix') +
                  ZeroOrMore(areaRangeOptions))('range')

#     +-shortcut
#       +-default [area (A.B.C.D|<0-4294967295>) shortcut (default|enable|disable)]
#       +-disable [area (A.B.C.D|<0-4294967295>) shortcut (default|enable|disable)]
#       +-enable [area (A.B.C.D|<0-4294967295>) shortcut (default|enable|disable)]
areaShortcutOptions = (Keyword('default') ^
                       Keyword('disable') ^
                       Keyword('enable'))
areaShortcut = Group(Keyword('shortcut') +
                     areaShortcutOptions)('shortcut')

#     +-stub [area (A.B.C.D|<0-4294967295>) stub]
#       +-no-summary [area (A.B.C.D|<0-4294967295>) stub no-summary]
areaStub = Group(Keyword('stub') +
                 Optional(Keyword('no-summary')))

#     +-virtual-link
#       +-A.B.C.D [area (A.B.C.D|<0-4294967295>) virtual-link A.B.C.D]
#         +-authentication [area (A.B.C.D|<0-4294967295>) virtual-link A.B.C.D {authentication (message-digest|null|)
#           |authentication-key LINE|message-digest-key <1-255> md5 LINE|dead-interval <1-65535>
#           |hello-interval <1-65535>|retransmit-interval <1-3600>|transmit-delay <1-3600>}]
#         +-authentication-key
#         +-dead-interval
#         +-hello-interval
#         +-message-digest-key
#         +-retransmit-interval
#         +-transmit-delay
areaVirtualLinkDeadInterval = (suppressedKeyword('dead-interval') +
                              naturalNumber('dead_interval'))
areaVirtualLinkHelloInterval = (suppressedKeyword('hello-interval') +
                               naturalNumber('hello_interval'))
areaVirtualLinkRetransmitInterval = (suppressedKeyword('retransmit-interval') +
                                     naturalNumber('retransmit_interval'))
areaVirtualLinkTransmitDelay = (suppressedKeyword('transmit-delay') +
                                naturalNumber('transmit_delay'))
areaVirtualLinkMessageDigestKey = (Keyword('message-digest-key') +
                                   naturalNumber('key_id') +
                                   Keyword('md5') +
                                   OneOrMore(Word(alphanums)('secret')))
areaVirtualLinkAuthentication = (Keyword('authentication') +
                                Optional(Keyword('null')))
areaVirtualLinkAuthenticationKey = (Keyword('authentication-key') +
                                   Word(alphanums)('key'))

areaVirtualLinkOptions = (areaVirtualLinkDeadInterval       ^
                          areaVirtualLinkHelloInterval      ^
                          areaVirtualLinkRetransmitInterval ^
                          areaVirtualLinkTransmitDelay      ^
                          areaVirtualLinkMessageDigestKey   ^
                          areaVirtualLinkAuthentication     ^
                          areaVirtualLinkAuthenticationKey)

areaVirtualLink = Group(suppressedKeyword('virtual-link') +
                        ipv4Address('address') +
                        ZeroOrMore(areaVirtualLinkOptions))('virtual_link')

areaOptions = (areaAuthentication ^
               areaDefaultCost    ^
               areaExportList     ^
               areaFilter         ^
               areaNssa           ^
               areaRange          ^
               areaShortcut       ^
               areaStub           ^
               areaVirtualLink)

area = Group(suppressedKeyword('area') +
             areaId +
             areaOptions)('area')

# +-auto-cost
#   +-reference-bandwidth
#     +-<1-4294967> [auto-cost reference-bandwidth <1-4294967>]
autoCost = Group(suppressedKeyword('auto-cost') +
                 suppressedKeyword('reference-bandwidth') +
                 naturalNumber('bandwidth'))

# +-compatible
#   +-rfc1583 [compatible rfc1583]
compatible = Group(suppressedKeyword('compatible') +
                   suppressedKeyword('rfc1583'))('compatible')

# +-default-information
#   +-originate [default-information originate]
#     +-always [default-information originate {metric <0-16777214>|metric-type (1|2)|?route-map WORD|always}]
#     +-metric
#     +-metric-type
#     +-route-map
defaultInformationOptionsMetric = (suppressedKeyword('metric') +
                                   naturalNumber('metric'))
defaultInformationOptionsMetricType = (suppressedKeyword('metric-type') +
                                       metricType('metric_type'))
defaultInformationOptionsRouteMap = (suppressedKeyword('route-map') +
                                     routeMapName('route_map'))
defaultInformationOptions = (Keyword('always') ^
                             defaultInformationOptionsMetric ^
                             defaultInformationOptionsMetricType ^
                             defaultInformationOptionsRouteMap)
defaultInformation = Group(suppressedKeyword('default-information') +
                           suppressedKeyword('originate') +
                           ZeroOrMore(defaultInformationOptions))('default_information')

# +-default-metric
#   +-<1-16777214> [default-metric <1-16777214>]
defaultMetric = Group(suppressedKeyword('default-metric') +
                 naturalNumber('metric'))('default_metric')

# +-distance
#   +-<1-255> [distance <1-255>]
#   +-ospf
#     +-external
#     +-inter-area
#     +-intra-area
distanceOspfTypes = (Keyword('external') ^
                     Keyword('inter-area') ^
                     Keyword('intra-area'))
distanceOspf = (Keyword('ospf') +
                OneOrMore(distanceOspfTypes +
                         naturalNumber('distance')))
distanceOptions = (naturalNumber('distance') ^
                   distanceOspf)
distance = Group(suppressedKeyword('distance') +
                 distanceOptions)('distance')

# +-distribute-list
#   +-WORD
#     +-in [distribute-list WORD in]
#     +-out
#       +-bgp [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-connected [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-intranet [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-isis [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-kernel [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-ospf [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#         +-<1-65535> [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-rip [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-static [distribute-list WORD out (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
distributeListProtocols = (Keyword('bgp')      ^
                          Keyword('connected') ^
                          Keyword('intranet')  ^
                          Keyword('isis')      ^
                          Keyword('kernel')    ^
                          Keyword('rip')       ^
                          Keyword('static')    ^
                          (Keyword('ospf') + Optional(naturalNumber('process_id'))))
distributeListIn = Keyword('in')
distributeListOut = (Keyword('out') +
                    distributeListProtocols)
distributeListOptions = (distributeListIn ^
                         distributeListOut)
distributeList = Group(suppressedKeyword('distribute-list') +
                       accesslistName('accesslist') +
                       distributeListOptions)('distribute_list')

# +-enable
#   +-db-summary-opt [enable db-summary-opt]
enable = Group(suppressedKeyword('enable') +
               suppressedKeyword('db-summary-opt'))('enable')

# +-host
#   +-A.B.C.D
#     +-area
#       +-<0-4294967295> [host A.B.C.D area (A.B.C.D|<0-4294967295>)]
#         +-cost
#           +-<0-65535> [host A.B.C.D area (A.B.C.D|<0-4294967295>) cost <0-65535>]
#       +-A.B.C.D [host A.B.C.D area (A.B.C.D|<0-4294967295>)]
#         +-cost
#           +-<0-65535> [host A.B.C.D area (A.B.C.D|<0-4294967295>) cost <0-65535>]
hostCost = (suppressedKeyword('cost') +
            naturalNumber('cost'))
host = Group(suppressedKeyword('host') +
             ipv4Address('address') +
             suppressedKeyword('area') +
             areaId('area') +
             Optional(hostCost))('host')

# +-max-concurrent-dd
#   +-<1-65535> [max-concurrent-dd <1-65535>]
maxConcurrentDD = Group(suppressedKeyword('max-concurrent-dd') +
                        naturalNumber('value'))('max_concurrent_dd')

# +-max-unuse-lsa
#   +-<0-65535> [max-unuse-lsa <0-65535>]
maxUnuseLsa = Group(suppressedKeyword('max-unuse-lsa') +
                    naturalNumber('value'))('max_unuse_lsa')

# +-max-unuse-packet
#   +-<0-65535> [max-unuse-packet <0-65535>]
maxUnusePacket = Group(suppressedKeyword('max-unuse-packet') +
                       naturalNumber('value'))('max_unuse_packet')

# +-maximum-area
#   +-<1-4294967294> [maximum-area <1-4294967294>]
maximumArea = Group(suppressedKeyword('maximum-area') +
                     naturalNumber('value'))('maximum_area')

# +-network
#   +-A.B.C.D
#     +-A.B.C.D
#       +-area
#         +-<0-4294967295> [network A.B.C.D A.B.C.D area (A.B.C.D|<0-4294967295>)]
#         +-A.B.C.D [network A.B.C.D A.B.C.D area (A.B.C.D|<0-4294967295>)]
#   +-A.B.C.D/M
#     +-area
#       +-<0-4294967295> [network A.B.C.D/M area (A.B.C.D|<0-4294967295>)]
#       +-A.B.C.D [network A.B.C.D/M area (A.B.C.D|<0-4294967295>)]
networkNetwork = (ipv4AddressNetwork ^
                  ipv4Prefix)
network = Group(suppressedKeyword('network') +
                networkNetwork('network') +
                suppressedKeyword('area') +
                areaId('area'))('network')

# +-opaque-lsa-capable [opaque-lsa-capable]
opaqueLsaCapable = Group(suppressedKeyword('opaque-lsa-capable'))('opaque_lsa_capable')

# +-ospf
#   +-abr-type
#     +-cisco [ospf abr-type (cisco|ibm|standard|shortcut)]
#     +-ibm [ospf abr-type (cisco|ibm|standard|shortcut)]
#     +-shortcut [ospf abr-type (cisco|ibm|standard|shortcut)]
#     +-standard [ospf abr-type (cisco|ibm|standard|shortcut)]
#   +-fib-install [ospf fib-install]
#   +-rfc1583compatibility [ospf rfc1583compatibility]
#   +-router-id
#     +-A.B.C.D [ospf router-id A.B.C.D]
ospfAbrTypeType = (Keyword('cisco')    ^
                   Keyword('ibm')      ^
                   Keyword('standard') ^
                   Keyword('shortcut'))
ospfAbrType = (suppressedKeyword('abr-type') +
               ospfAbrTypeType)
ospfFibInstall = suppressedKeyword('fib-install')('fib_install')
ospfCompatibility = Keyword('rfc1583compatibility')
ospfRouterId = (suppressedKeyword('router-id') +
                ipv4Address('router_id'))
ospfOptions = (ospfAbrType       ^
               ospfFibInstall    ^
               ospfCompatibility ^
               ospfRouterId)
ospf = Group(Optional(suppressedKeyword('no')) +
             suppressedKeyword('ospf') +
             ospfOptions)('ospf')

# +-passive-interface [passive-interface (IFNAME A.B.C.D |)]
#   +-IFNAME [passive-interface IFNAME]
#     +-A.B.C.D [passive-interface (IFNAME A.B.C.D |)]
passiveInterface = Group(suppressedKeyword('passive-interface') +
                         interfaceName('interface') +
                         Optional(ipv4Address('ipaddress')))('passive_interface')

# +-redistribute
#   +-bgp [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-connected [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-intranet [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-isis [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-kernel [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-ospf [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-<1-65535> [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#       +-metric
#       +-metric-type
#       +-route-map
#       +-tag
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-rip [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
#   +-static [redistribute (kernel|connected|static|rip|bgp|isis|ospf (<1-65535>|)|intranet)]
#     +-metric
#     +-metric-type
#     +-route-map
#     +-tag
redistributeMetric = (suppressedKeyword('metric') +
                      naturalNumber('metric'))
metricType = (Keyword('1') ^
              Keyword('2'))
redistributeMetricType = (suppressedKeyword('metric-type') +
                          metricType)
redistributeTag = (suppressedKeyword('tag') +
                   naturalNumber)
redistributeRouteMap = (suppressedKeyword('route-map') +
                        routeMapName)

redistributeOptions = (Optional(redistributeMetric, default=None)('metric') +
                       Optional(redistributeMetricType, default=None)('type') +
                       Optional(redistributeTag, default=None)('tag') +
                       Optional(redistributeRouteMap, default=None)('route_map'))
redistributeKeyword = suppressedKeyword('redistribute')
redistributeBGP = Group(redistributeKeyword +
                        suppressedKeyword('bgp') +
                        redistributeOptions)
redistributeConnected = Group(redistributeKeyword +
                              suppressedKeyword('connected') +
                              redistributeOptions)
redistributeIntranet = Group(redistributeKeyword +
                             suppressedKeyword('intranet') +
                             redistributeOptions)
redistributeISIS = Group(redistributeKeyword +
                         suppressedKeyword('isis') +
                         redistributeOptions)
redistributeKernel = Group(redistributeKeyword +
                           suppressedKeyword('kernel') +
                           redistributeOptions)
redistributeOSPF = Group(redistributeKeyword +
                         suppressedKeyword('ospf') +
                         Optional(naturalNumber('process_id'), default=0) +
                         redistributeOptions)
redistributeRIP = Group(redistributeKeyword +
                        suppressedKeyword('rip') +
                        redistributeOptions)
redistributeStatic = Group(redistributeKeyword +
                           suppressedKeyword('static') +
                           redistributeOptions)


redistribute = (Optional(redistributeBGP, default=None)('bgp') +
                Optional(redistributeConnected, default=None)('connected') +
                Optional(redistributeIntranet, default=None)('intranet') +
                Optional(redistributeISIS, default=None)('isis') +
                Optional(redistributeKernel, default=None)('kernel') +
                Optional(redistributeOSPF, default=None)('ospf') +
                Optional(redistributeRIP, default=None)('rip') +
                Optional(redistributeStatic, default=None)('static'))

# +-refresh
#   +-timer
#     +-<10-1800> [refresh timer <10-1800>]
refresh = Group(suppressedKeyword('refresh') +
                suppressedKeyword('timer') +
                naturalNumber('timer'))('refresh_timer')

# +-summary-address
#   +-A.B.C.D/M [summary-address A.B.C.D/M (not-advertise|tag <0-4294967295>|)]
#     +-not-advertise [summary-address A.B.C.D/M (not-advertise|tag <0-4294967295>|)]
#     +-tag
#       +-<0-4294967295> [summary-address A.B.C.D/M (not-advertise|tag <0-4294967295>|)]
summaryAddressTag = (suppressedKeyword('tag') +
                     naturalNumber('tag'))
summaryAddressOptions = (Keyword('not-advertise') ^
                        summaryAddressTag)
summaryAddress = Group(suppressedKeyword('summary-address') +
                       ipv4Prefix('network') +
                       Optional(summaryAddressOptions))('summary_address')

# +-timers
#   +-spf
#     +-<0-2147483647>
#       +-<0-2147483647> [timers spf <0-2147483647> <0-2147483647>]
#     +-exp
#       +-<0-2147483647>
#         +-<0-2147483647> [timers spf exp <0-2147483647> <0-2147483647>]
timers = Group(Keyword('timers') +
               Keyword('spf') +
               Optional(Keyword('exp')) +
               naturalNumber('delay') +
               naturalNumber('hold'))

ospfTokens = (ZeroOrMore(ospf) +
              ZeroOrMore(compatible) +
              ZeroOrMore(autoCost) +
              Optional(maxConcurrentDD) +
              ZeroOrMore(enable) +
              ZeroOrMore(enable) +
              Group(redistribute)('redistribute') +
              Group(ZeroOrMore(passiveInterface))('passive_interfaces') +
              Optional(maximumArea) +
              ZeroOrMore(host) +
              Group(ZeroOrMore(area))('areas') +
              Group(ZeroOrMore(network))('networks') +
              ZeroOrMore(defaultMetric) +
              ZeroOrMore(distributeList) +
              ZeroOrMore(defaultInformation) +
              ZeroOrMore(distance) +
              Group(ZeroOrMore(summaryAddress))('summary_addresses') +

              Optional(maxUnuseLsa) +
              Optional(maxUnusePacket) +
              Optional(opaqueLsaCapable) +
              Optional(refresh) +
              Optional(timers))

routerOSPF = Group(suppressedKeyword('router') +
                   suppressedKeyword('ospf') +
                   Optional(naturalNumber('process'), default='0') +
                   ospfTokens)('router_ospf')
