# -*- coding: utf-8 -*-
# The MIT License (MIT)

# Copyright (c) 2015 Aleksandar Topuzović <aleksandar.topuzovic@gmail.com>

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

from pyparsing import (Literal, Keyword, Group, Optional, OneOrMore, ZeroOrMore,
                       Word, alphanums, SkipTo, LineEnd, Suppress)
from ...common import (ipv4Address, ipv6Address, ipv4Prefix, naturalNumber,
                      suppressedKeyword, routeMapName, accesslistName,
                      interfaceName)

direction = (Keyword('in') ^
             Keyword('out'))('direction')

# +-auto-summary [auto-summary]
autoSummary = Keyword('auto-summary')

# +-bgp
#   +-always-compare-med [bgp always-compare-med]
bgpAlwaysCompareMed = Keyword('always-compare-med')

# +-bgp
#   +-bestpath
#     +-as-path
#       +-ignore [bgp bestpath as-path ignore]
#     +-compare-confed-aspath [bgp bestpath compare-confed-aspath]
#     +-compare-routerid [bgp bestpath compare-routerid]
#     +-med
#       +-confed [bgp bestpath med (confed|missing-as-worst|remove-recv-med|remove-send-med )]
#         +-missing-as-worst [bgp bestpath med confed missing-as-worst]
#       +-missing-as-worst [bgp bestpath med (confed|missing-as-worst|remove-recv-med|remove-send-med )]
#         +-confed [bgp bestpath med missing-as-worst confed]
#       +-remove-recv-med [bgp bestpath med (confed|missing-as-worst|remove-recv-med|remove-send-med )]
#       +-remove-send-med [bgp bestpath med (confed|missing-as-worst|remove-recv-med|remove-send-med )]
bgpBestpathAsPathIgnore = (Keyword('as-path') +
                           Keyword('ignore'))
bgpBestpathCompareConfedAspath = Keyword('compare-confed-aspath')
bgpBestpathCompareRouterID = Keyword('compare-routerid')
removeRecvMed = Keyword('remove-recv-med')
removeSendMed = Keyword('remove-send-med')
bgpBestpathMed = (suppressedKeyword('med') +
                  Optional(removeRecvMed ^
                           removeSendMed))
bgpBestPathOptions = (bgpBestpathAsPathIgnore ^
                      bgpBestpathCompareConfedAspath ^
                      bgpBestpathCompareRouterID)
bgpBestPath = Group(suppressedKeyword('bestpath') +
                    Optional(bgpBestPathOptions))

# +-bgp
#   +-client-to-client
#     +-reflection [bgp client-to-client reflection]
bgpClientToClientReflection = Group(Keyword('client-to-client') +
                                    Keyword('reflection'))('client_to_client')

# +-bgp
#   +-cluster-id
#     +-<1-4294967295> [bgp cluster-id <1-4294967295>]
#     +-A.B.C.D [bgp cluster-id A.B.C.D]
clusterId = (ipv4Address ^
             naturalNumber)
bgpClusterId = Group(suppressedKeyword('cluster-id') +
                     clusterId('clusterid'))('clusterid')

# +-bgp
#   +-confederation
#     +-identifier
#       +-<1-65535> [bgp confederation identifier <1-65535>]
#     +-peers
#       +-<1-65535> [bgp confederation peers .<1-65535>]
bgpConfederationType = (Keyword('identifier') ^
                        Keyword('peers'))
bgpConfederation = Group(suppressedKeyword('confederation') +
                         bgpConfederationType +
                         naturalNumber('value'))('confederation')

# +-bgp
#   +-dampening [bgp dampening]
#     +-<1-45> [bgp dampening <1-45>]
#       +-<1-20000>
#         +-<1-20000>
#           +-<1-255> [bgp dampening <1-45> <1-20000> <1-20000> <1-255>]
#             +-<1-45> [bgp dampening <1-45> <1-20000> <1-20000> <1-255> <1-45>]
#     +-route-map
#       +-WORD [bgp dampening route-map WORD]
bgpDampeningNum = (naturalNumber('half-life') +
                   Optional(naturalNumber)('reuse') +
                   Optional(naturalNumber)('suppress') +
                   Optional(naturalNumber)('max-suppress-time') +
                   Optional(naturalNumber)('ur-half-life'))
bgpDampeningRouteMap = (suppressedKeyword('route-map') +
                        routeMapName('route-map'))
bgpDampeningOptions = (bgpDampeningNum ^
                       bgpDampeningRouteMap)
bgpDampening = (Keyword('dampening') +
                Optional(bgpDampeningOptions))

# +-bgp
#   +-default
#     +-ipv4-unicast [bgp default ipv4-unicast]
#     +-local-preference
#       +-<0-4294967295> [bgp default local-preference <0-4294967295>]
bgpDefaultIPv4Unicast = Keyword('ipv4-unicast')
bgpDefaultLocalPreference = (suppressedKeyword('local-preference') +
                          naturalNumber('local-preference'))
bgpDefaultOptions = (bgpDefaultIPv4Unicast ^
                     bgpDefaultLocalPreference)
bgpDefault = (Keyword('default') +
              bgpDefaultOptions)

# +-bgp
#   +-deterministic-med [bgp deterministic-med]
bgpDeterministicMed = Keyword('deterministic-med')

# +-bgp
#   +-enforce-first-as [bgp enforce-first-as]
bgpEnforceFirstAs = Keyword('enforce-first-as')

# +-bgp
#   +-fast-external-failover [bgp fast-external-failover]
bgpFastExternalFailover = Keyword('fast-external-failover')

# +-bgp
#   +-graceful-restart [bgp graceful-restart]
#     +-graceful-reset [bgp graceful-restart graceful-reset]
#     +-restart-time
#       +-<1-3600> [bgp graceful-restart restart-time <1-3600>]
#     +-stalepath-time
#       +-<1-3600> [bgp graceful-restart stalepath-time <1-3600>]
bgpGracefulRestartGracefulReset = Keyword('graceful-restart')
bgpGracefulRestartRestartTime = (suppressedKeyword('restart-time') +
                                 naturalNumber('restart_time'))
bgpGracefulRestartStalePathTime = (suppressedKeyword('stalepath-time') +
                                   naturalNumber('stalepath_time'))
bgpGracefulRestartOptions = (bgpGracefulRestartGracefulReset ^
                             bgpGracefulRestartRestartTime ^
                             bgpGracefulRestartStalePathTime)
bgpGracefulRestart = (Keyword('graceful-restart') +
                      Optional(bgpGracefulRestartOptions))

# +-bgp
#   +-log-neighbor-changes [bgp log-neighbor-changes]
bgpLogNeighborChnages = Keyword('log-neighbor-changes')

# +-bgp
#   +-nexthop-trigger-count
#     +-<0-127> [bgp nexthop-trigger-count <0-127>]
bgpNexthopTriggerCount = (suppressedKeyword('nexthop-trigger-count') +
                          naturalNumber('nexthop_trigger_count'))

# +-bgp
#   +-router-id
#     +-A.B.C.D [bgp router-id A.B.C.D]
bgpRouterId = (suppressedKeyword('router-id') +
               ipv4Address('router_id'))

# +-bgp
#   +-scan-time
#     +-<0-60> [bgp scan-time <0-60>]
bgpRouterScanTime = (suppressedKeyword('scan-time') +
                     naturalNumber('scan_time'))

# +-bgp
#   +-update-delay
#     +-<1-3600> [bgp update-delay <1-3600>]
bgpRouterUpdateDelay = (suppressedKeyword('scan-delay') +
                     naturalNumber('scan_delay'))

bgpOptions = (bgpAlwaysCompareMed         ^
              bgpBestPath                 ^
              bgpClientToClientReflection ^
              bgpClusterId                ^
              bgpConfederation            ^
              bgpDampening                ^
              bgpDefault                  ^
              bgpDeterministicMed         ^
              bgpEnforceFirstAs           ^
              bgpFastExternalFailover     ^
              bgpGracefulRestart          ^
              bgpLogNeighborChnages       ^
              bgpNexthopTriggerCount      ^
              bgpRouterId                 ^
              bgpRouterScanTime           ^
              bgpRouterUpdateDelay)

bgp = Group(Optional(Keyword('no'), default='yes')('enabled') +
            suppressedKeyword('bgp') +
            bgpOptions)('option')

# +-distance
#   +-<1-255>
#     +-A.B.C.D/M [distance <1-255> A.B.C.D/M]
#       +-WORD [distance <1-255> A.B.C.D/M WORD]
#   +-bgp
#     +-<1-255>
#       +-<1-255>
#         +-<1-255> [distance bgp <1-255> <1-255> <1-255>]
distanceOptionsNum = (naturalNumber +
                      ipv4Prefix +
                      Word(alphanums))
distanceOptionsBgp = (Keyword('bgp') +
                      naturalNumber +
                      naturalNumber +
                      naturalNumber)
distanceOptions = (distanceOptionsNum ^
                   distanceOptionsBgp)
distance = (suppressedKeyword('distance') +
            distanceOptions)

# +-neighbor
#   +-A.B.C.D
#     +-activate [neighbor (A.B.C.D|X:X::X:X|WORD) activate]
neighbourActivate = Keyword('activate')

#     +-advertisement-interval
#       +-<0-600> [neighbor (A.B.C.D|X:X::X:X|WORD) advertisement-interval <0-600>]
neighbourAdvertismentInterval = (suppressedKeyword('advertisement-interval') +
                                 naturalNumber('advertisement_interval'))

#     +-allowas-in [neighbor (A.B.C.D|X:X::X:X|WORD) allowas-in]
#       +-<1-10> [neighbor (A.B.C.D|X:X::X:X|WORD) allowas-in <1-10>]
neighbourAllowasIn = (suppressedKeyword('allowas-in') +
                      naturalNumber('allowas_in'))

#     +-as-origination-interval
#       +-<1-600> [neighbor (A.B.C.D|X:X::X:X|WORD) as-origination-interval <1-600>]
neighbourAsOriginationinterval = (suppressedKeyword('as-origination-interval') +
                                  naturalNumber('as_origination_interval'))

#     +-attribute-unchanged [neighbor (A.B.C.D|X:X::X:X|WORD) attribute-unchanged ({ as-path|next-hop|med }|)]
#       +-as-path [neighbor (A.B.C.D|X:X::X:X|WORD) attribute-unchanged ({ as-path|next-hop|med }|)]
#       +-med [neighbor (A.B.C.D|X:X::X:X|WORD) attribute-unchanged ({ as-path|next-hop|med }|)]
#       +-next-hop [neighbor (A.B.C.D|X:X::X:X|WORD) attribute-unchanged ({ as-path|next-hop|med }|)]
neighbourAttributeUnchangedOptions = (Keyword('as-path') ^
                                      Keyword('med')     ^
                                      Keyword('next-hop'))
neighbourAttributeUnchanged = (suppressedKeyword('attribute-unchanged') +
                               ZeroOrMore(neighbourAttributeUnchangedOptions))
#     +-capability
#       +-dynamic [neighbor (A.B.C.D|X:X::X:X|WORD) capability dynamic]
#       +-graceful-restart [neighbor (A.B.C.D|X:X::X:X|WORD) capability graceful-restart]
#       +-orf
#         +-prefix-list
#           +-both [neighbor (A.B.C.D|X:X::X:X|WORD) capability orf prefix-list (both|receive|send)]
#           +-receive [neighbor (A.B.C.D|X:X::X:X|WORD) capability orf prefix-list (both|receive|send)]
#           +-send [neighbor (A.B.C.D|X:X::X:X|WORD) capability orf prefix-list (both|receive|send)]
#       +-route-refresh [neighbor (A.B.C.D|X:X::X:X|WORD) capability route-refresh]

#     +-collide-established [neighbor (A.B.C.D|X:X::X:X|WORD) collide-established]
neighbourCollideEstablished = Keyword('collide-established')

#     +-connection-retry-time
#       +-<1-65535> [neighbor (A.B.C.D|X:X::X:X|WORD) connection-retry-time <1-65535>]
neighbourConnextionRetryTime = (suppressedKeyword('connection-retry-time') +
                                naturalNumber('connection_retry_time'))

#     +-default-originate [neighbor (A.B.C.D|X:X::X:X|WORD) default-originate]
#       +-route-map
#         +-WORD [neighbor (A.B.C.D|X:X::X:X|WORD) default-originate route-map WORD]
neighbourDefaultOriginate = Group(suppressedKeyword('default-originate') +
                                  suppressedKeyword('route-map') +
                                  routeMapName('route-map'))('default_originate')
#     +-description
#       +-LINE [neighbor (A.B.C.D|X:X::X:X|WORD) description LINE]
neighbourDescription = (suppressedKeyword('description') +
                        SkipTo(LineEnd())('description'))

#     +-disallow-infinite-holdtime [neighbor (A.B.C.D|X:X::X:X|WORD) disallow-infinite-holdtime]
neighbourDisallowInfiniteHoldTime = Keyword('disallow-infinite-holdtime')

#     +-distribute-list
#       +-<1-199>
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
#       +-<1300-2699>
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
#       +-WORD
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) distribute-list (<1-199>|<1300-2699>|WORD) (in|out)]
neighbourDistributeList = Group(suppressedKeyword('distribute-list') +
                                accesslistName('accesslist') +
                                direction)('distribute_list')

#     +-dont-capability-negotiate [neighbor (A.B.C.D|X:X::X:X|WORD) dont-capability-negotiate]
neighbourDontCapabilityNegotiate = Keyword('dont-capability-negotiate')

#     +-ebgp-multihop [neighbor (A.B.C.D|X:X::X:X|WORD) ebgp-multihop]
#       +-<1-255> [neighbor (A.B.C.D|X:X::X:X|WORD) ebgp-multihop <1-255>]
neighbourEbgpMultihop = (Keyword('ebgp-multihop') +
                         naturalNumber('hops'))

#     +-enforce-multihop [neighbor (A.B.C.D|X:X::X:X|WORD) enforce-multihop]
neighbourEnforceMultihop = Keyword('enforce-multihop')

#     +-filter-list
#       +-WORD
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) filter-list WORD (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) filter-list WORD (in|out)]
neighbourFilterList = (suppressedKeyword('filter-list') +
                       Word(alphanums) +
                       direction)

#     +-interface
#       +-WORD [neighbor (A.B.C.D|X:X::X:X) interface WORD]
neighbourInterface = (suppressedKeyword('interface') +
                      interfaceName('interface'))

#     +-maximum-prefix
#       +-<1-4294967295> [neighbor (A.B.C.D|X:X::X:X|WORD) maximum-prefix <1-4294967295>]
#         +-<1-100> [neighbor (A.B.C.D|X:X::X:X|WORD) maximum-prefix <1-4294967295> <1-100>]
#           +-warning-only [neighbor (A.B.C.D|X:X::X:X|WORD) maximum-prefix <1-4294967295> <1-100> warning-only]
#         +-warning-only [neighbor (A.B.C.D|X:X::X:X|WORD) maximum-prefix <1-4294967295> warning-only]
warningOnly = Keyword('warning-only')
neighbourMaximumPrefixOptions = ((naturalNumber('num') +
                                  warningOnly) ^
                                 warningOnly)
neighbourMaximumPrefix = Group(suppressedKeyword('maximum-prefix') +
                               naturalNumber('maximum_prefix') +
                               Optional(neighbourMaximumPrefixOptions))

#     +-next-hop-self [neighbor (A.B.C.D|X:X::X:X|WORD) next-hop-self]
neighbourNextHopSelf = Keyword('next-hop-self')

#     +-override-capability [neighbor (A.B.C.D|X:X::X:X|WORD) override-capability]
neighbourOverrideCapability = Keyword('override-capability')

#     +-passive [neighbor (A.B.C.D|X:X::X:X|WORD) passive]
neighbourPassive = Keyword('passive')

#     +-peer-group
#       +-WORD [neighbor (A.B.C.D|X:X::X:X) peer-group WORD]
neighbourPeerGroup = (suppressedKeyword('peer-group') +
                      naturalNumber('peer_group'))

#     +-port
#       +-<0-65535> [neighbor (A.B.C.D|X:X::X:X|WORD) port <0-65535>]
neighbourPort = (suppressedKeyword('port') +
                 naturalNumber('port'))

#     +-prefix-list
#       +-WORD
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) prefix-list WORD (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) prefix-list WORD (in|out)]
neighbourPrefixList = Group(suppressedKeyword('prefix-list') +
                            Word(alphanums)('prefix_list') +
                            direction)('prefix_list')

#     +-remote-as
#       +-<1-4294967295> [neighbor (A.B.C.D|X:X::X:X|WORD) remote-as <1-4294967295>]
neighbourRemoteAs = (suppressedKeyword('remote-as') +
                     naturalNumber('remote-as'))

#     +-remove-private-AS [neighbor (A.B.C.D|X:X::X:X|WORD) remove-private-AS]
neighbourRemotePrivateAs = Keyword('remove-private-AS')

#     +-restart-time
#       +-<1-3600> [neighbor (A.B.C.D|X:X::X:X|WORD) restart-time <1-3600>]
neighbourRestartTime = (suppressedKeyword('restart-time') +
                        naturalNumber('restart_time'))

#     +-route-map
#       +-WORD
#         +-in [neighbor (A.B.C.D|X:X::X:X|WORD) route-map WORD (in|out)]
#         +-out [neighbor (A.B.C.D|X:X::X:X|WORD) route-map WORD (in|out)]
neighbourRouteMap = (suppressedKeyword('route-map') +
                     routeMapName('route-map') +
                     direction)

#     +-route-reflector-client [neighbor (A.B.C.D|X:X::X:X|WORD) route-reflector-client]
neighbourRouteReflectorClient = Keyword('route-reflector-client')

#     +-route-server-client [neighbor (A.B.C.D|X:X::X:X|WORD) route-server-client]
neighbourRouteServerClient = Keyword('route-server-client')

#     +-send-community [neighbor (A.B.C.D|X:X::X:X|WORD) send-community]
#       +-both [neighbor (A.B.C.D|X:X::X:X|WORD) send-community (both|extended|standard)]
#       +-extended [neighbor (A.B.C.D|X:X::X:X|WORD) send-community (both|extended|standard)]
#       +-standard [neighbor (A.B.C.D|X:X::X:X|WORD) send-community (both|extended|standard)]
neighbourSendCommunityOptions = (Keyword('both') ^
                                 Keyword('extended') ^
                                 Keyword('standard'))
neighbourSendCommunity = Group(suppressedKeyword('send-community') +
                               ZeroOrMore(neighbourSendCommunityOptions))

#     +-shutdown [neighbor (A.B.C.D|X:X::X:X|WORD) shutdown]
neighbourShutdown = Keyword('shutdown')

#     +-soft-reconfiguration
#       +-inbound [neighbor (A.B.C.D|X:X::X:X|WORD) soft-reconfiguration inbound]
neighbourSoftReconfiguration = (Keyword('soft-reconfiguration') +
                                Keyword('inbound'))

#     +-strict-capability-match [neighbor (A.B.C.D|X:X::X:X|WORD) strict-capability-match]
neighbourStrictCapabilityMatch = Keyword('strict-capability-match')
#     +-timers
#       +-<0-65535>
#         +-<0-65535> [neighbor (A.B.C.D|X:X::X:X|WORD) timers <0-65535> <0-65535>]
#       +-connect
#         +-<1-65535> [neighbor (A.B.C.D|X:X::X:X|WORD) timers connect <1-65535>]
neighbourTimersRegular = (naturalNumber('keepalive') +
                          naturalNumber('holdtime'))
neighbourTimersConnect = (suppressedKeyword('connect') +
                          naturalNumber('connect'))
neighbourTimers = Group(neighbourTimersRegular ^
                        neighbourTimersConnect)('timers')

#     +-transparent-as [neighbor (A.B.C.D|X:X::X:X|WORD) transparent-as]
neighbourTransparentAs = Keyword('transparent-as')

#     +-transparent-nexthop [neighbor (A.B.C.D|X:X::X:X|WORD) transparent-nexthop]
neighbourTransparentNextHop = Keyword('transparent-nexthop')

#     +-unsuppress-map
#       +-WORD [neighbor (A.B.C.D|X:X::X:X|WORD) unsuppress-map WORD]
neighbourUnsuppressMap = (suppressedKeyword('unsuppress-map') +
                          Word(alphanums)('unsuppress_map'))

#     +-update-source
#       +-WORD [neighbor (A.B.C.D|X:X::X:X|WORD) update-source WORD]
neighbourUpdateSource = (suppressedKeyword('update-source') +
                         Word(alphanums)('update_source'))
#     +-version
#       +-4 [neighbor (A.B.C.D|X:X::X:X|WORD) version (4)]
neighbourVersion = (suppressedKeyword('version') +
                    naturalNumber('version'))
#     +-weight
#       +-<0-65535> [neighbor (A.B.C.D|X:X::X:X|WORD) weight <0-65535>]
neighbourWeight = (suppressedKeyword('weight') +
                   naturalNumber('weight'))

neighbourOptions = (neighbourActivate                 ^
                    neighbourAdvertismentInterval     ^
                    neighbourAllowasIn                ^
                    neighbourAsOriginationinterval    ^
                    neighbourAttributeUnchanged       ^
                    neighbourCollideEstablished       ^
                    neighbourConnextionRetryTime      ^
                    neighbourDefaultOriginate         ^
                    neighbourDescription              ^
                    neighbourDisallowInfiniteHoldTime ^
                    neighbourDistributeList           ^
                    neighbourDontCapabilityNegotiate  ^
                    neighbourEbgpMultihop             ^
                    neighbourEnforceMultihop          ^
                    neighbourFilterList               ^
                    neighbourInterface                ^
                    neighbourMaximumPrefix            ^
                    neighbourNextHopSelf              ^
                    neighbourOverrideCapability       ^
                    neighbourPassive                  ^
                    neighbourPeerGroup                ^
                    neighbourPort                     ^
                    neighbourPrefixList               ^
                    neighbourRemoteAs                 ^
                    neighbourRemotePrivateAs          ^
                    neighbourRestartTime              ^
                    neighbourRouteMap                 ^
                    neighbourRouteReflectorClient     ^
                    neighbourRouteServerClient        ^
                    neighbourSendCommunity            ^
                    neighbourShutdown                 ^
                    neighbourSoftReconfiguration      ^
                    neighbourStrictCapabilityMatch    ^
                    neighbourTimers                   ^
                    neighbourTransparentAs            ^
                    neighbourTransparentNextHop       ^
                    neighbourUnsuppressMap            ^
                    neighbourUpdateSource             ^
                    neighbourVersion                  ^
                    neighbourWeight)
neighbourId = (ipv4Address('ipv4') ^
               ipv6Address('ipv6') ^
               Word(alphanums)('group'))
neighbour = Group(suppressedKeyword('neighbor') +
                  neighbourId +
                  neighbourOptions)('neighbour')

# +-network
#   +-A.B.C.D [network A.B.C.D (backdoor|)]
#     +-backdoor [network A.B.C.D (backdoor|)]
#     +-mask
#       +-A.B.C.D [network A.B.C.D mask A.B.C.D (backdoor|)]
#         +-backdoor [network A.B.C.D mask A.B.C.D (backdoor|)]
#         +-route-map
#           +-WORD [network A.B.C.D  mask A.B.C.D route-map WORD (backdoor|)]
#             +-backdoor [network A.B.C.D  mask A.B.C.D route-map WORD (backdoor|)]
#     +-route-map
#       +-WORD [network A.B.C.D route-map WORD (backdoor|)]
#         +-backdoor [network A.B.C.D route-map WORD (backdoor|)]
#   +-A.B.C.D/M [network A.B.C.D/M (backdoor|)]
#     +-backdoor [network A.B.C.D/M (backdoor|)]
#     +-route-map
#       +-WORD [network A.B.C.D/M route-map WORD (backdoor|)]
#         +-backdoor [network A.B.C.D/M route-map WORD (backdoor|)]
#   +-synchronization [network synchronization]
networkBackdoor = Keyword('backdoor')
networkRouteMap = (suppressedKeyword('route-map') +
                   routeMapName)
networkMask = (suppressedKeyword('mask') +
               ipv4Address('netmask'))
networkAddressOptions = (Optional(networkMask) +
                         Optional(networkRouteMap) +
                         Optional(networkBackdoor))
networkAddress = (ipv4Address('network') +
                 networkAddressOptions)
networkPrefixOptions = (Optional(networkRouteMap) +
                        Optional(networkBackdoor))
networkPrefix = (ipv4Prefix('prefix') +
                 networkPrefixOptions)
networkOptions = (networkAddress ^
                  networkPrefix ^
                  Keyword('synchronization'))
network = (Keyword('network') +
           networkOptions)

# +-address-family
#   +-ipv4 [address-family ipv4]
#     +-multicast [address-family ipv4 multicast]
#     +-unicast [address-family ipv4 unicast]
#   +-ipv6 [address-family ipv6 (unicast|)]
#     +-unicast [address-family ipv6 (unicast|)]
unicast = Keyword('unicast')
multicast = Keyword('multicast')
addressFamilyIPv4 = (Keyword('ipv4') +
                     Optional(unicast ^
                              multicast))
addressFamilyIPv6 = (Keyword('ipv6') +
                     Optional(unicast))
addressFamilyOptions = (addressFamilyIPv4 ^
                        addressFamilyIPv6)
addressFamily = (suppressedKeyword('address-family') +
                 addressFamilyOptions)('address-family')

exitAddressFamily = Keyword('exit-address-family')

# +-aggregate-address
#   +-A.B.C.D/M [aggregate-address A.B.C.D/M]
#     +-as-set [aggregate-address A.B.C.D/M as-set]
#       +-summary-only [aggregate-address A.B.C.D/M as-set summary-only]
#     +-summary-only [aggregate-address A.B.C.D/M summary-only]
#       +-as-set [aggregate-address A.B.C.D/M summary-only as-set]
aggregateAddressOptions = (Keyword('as-set') ^
                           Keyword('summary-only'))
aggregateAddress = Group(suppressedKeyword('aggregate-address') +
                         ipv4Prefix('prefix') +
                         ZeroOrMore(aggregateAddressOptions))('aggregate-address')

# +-redistribute
#   +-connected [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-intranet [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-isis [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-kernel [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-ospf [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-rip [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
#   +-static [redistribute (kernel|connected|static|rip|ospf|isis|intranet)]
#     +-route-map
#       +-WORD [redistribute (kernel|connected|static|rip|ospf|isis|intranet) route-map WORD]
redistributeProtocol = (Keyword('bgp')       ^
                        Keyword('connected') ^
                        Keyword('intranet')  ^
                        Keyword('isis')      ^
                        Keyword('kernel')    ^
                        Keyword('ospf')      ^
                        Keyword('rip')       ^
                        Keyword('static'))

redistribute = Group(suppressedKeyword('redistribute') +
                     redistributeProtocol('protocol') +
                     Optional(suppressedKeyword('route-map') +
                              routeMapName('routemap')))('redistribute')

# +-synchronization [synchronization]
synchronization = Keyword('synchronization')

# +-timers
#   +-bgp
#     +-<0-65535>
#       +-<0-65535> [timers bgp <0-65535> <0-65535>]
timers = Group(suppressedKeyword('timers') +
               suppressedKeyword('bgp') +
               naturalNumber('keepalive') +
               naturalNumber('holdtime'))('timers')

addressFamilyJoined = (
    addressFamily + (
        autoSummary ^
        Group(ZeroOrMore(neighbour))('neighbours') ^
        Group(ZeroOrMore(network))('networks')) +
    Suppress(exitAddressFamily)
)

bgpIgnoreLine = Suppress(Literal('!') +
                         SkipTo(LineEnd()))

bgpTokens = (
    autoSummary ^
    Group(bgp)('bgp') ^
    distance ^
    Group(OneOrMore(neighbour))('neighbours') ^
    Group(OneOrMore(network))('networks') ^
    # addressFamily ^
    # exitAddressFamily ^
    Group(addressFamilyJoined)('address-family') ^
    aggregateAddress ^
    Group(OneOrMore(redistribute))('redistributes') ^
    synchronization ^
    timers ^
    bgpIgnoreLine
)

routerBGP = Group(suppressedKeyword('router') +
                  suppressedKeyword('bgp') +
                  naturalNumber('as_number')  +
                  ZeroOrMore(bgpTokens))('router_bgp')
