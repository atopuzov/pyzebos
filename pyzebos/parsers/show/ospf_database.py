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

from pyparsing import (OneOrMore, Group, Combine, Optional, Suppress, Literal,
                       Word, SkipTo, LineEnd, nums, hexnums)
from ..common import ipv4Address

hexNumber = Combine(Optional(Literal('0x')) +
                    Word(hexnums))

lsaAge = (Suppress(Literal('LS age:')) +
          Word(nums)('ls_age'))

lsaOptions = (Suppress(Literal('Options:')) +
              hexNumber('options') +
              Suppress(SkipTo(LineEnd())))

lsaFlags = (Suppress(Literal('Flags:')) +
            hexNumber('flags') +
            Optional(Suppress(Literal(':')) + SkipTo(LineEnd())))

lsaTypes = (Literal('router-LSA') ^
            Literal('network-LSA') ^
            Literal('summary-LSA') ^
            Literal('AS-external-LSA'))

lsaType = (Suppress(Literal('LS Type:')) +
          lsaTypes('lsa_type'))

lsaId = (Suppress(Literal('Link State ID:')) +
         ipv4Address('link_state_id') +
         Suppress(SkipTo(LineEnd())))

lsaAdvRouter = (Suppress(Literal('Advertising Router:')) +
                ipv4Address('advertising_router'))

lsaSeqNum = (Suppress(Literal('LS Seq Number:')) +
            hexNumber('seqnumber'))

lsaCheksum = (Suppress(Literal('Checksum:')) +
             hexNumber('checksum'))

lsaLength = (Suppress(Literal('Length:')) +
            Word(nums)('length'))

lsaNetworkM = (Suppress(Literal('Network Mask:')) +
               Suppress(Literal('/')) +
               Word(nums)('network_mask'))

lsaMetricType = (Suppress(Literal('Metric Type:')) +
                 Word(nums)('metric_type') +
                 Suppress(SkipTo(LineEnd())))

lsaTOS = (Suppress(Literal('TOS:')) +
          Word(nums)('tos'))

lsaMetric = (Suppress(Literal('Metric:')) +
             Word(nums)('metric'))

lsaFwdAddres = (Suppress(Literal('Forward Address:')) +
                ipv4Address('forward_address'))

lsaAttRouter = (Suppress(Literal('Attached Router:')) +
                ipv4Address('attached_router'))

lsaNumberOfL = (Suppress(Literal('Number of Links:')) +
                Word(nums)('number_of_links'))

lsaRouteTag = (Suppress(Literal('External Route Tag:')) +
               Word(nums)('external_route_tag'))

lsaTosMetric = (Suppress(Literal('TOS:')) +
                Word(nums)('TOS') +
                Suppress(Literal('Metric:')) +
                Word(nums)('metric'))

lsaLinkStub = (Suppress(Literal('(Link ID) Network/subnet number:')) +
               ipv4Address('network_number') +
               Suppress(Literal('(Link Data) Network Mask:')) +
               ipv4Address('network_mask'))

lsaLinkRouter = (Suppress(Literal('(Link ID) Neighboring Router ID:')) +
                 ipv4Address('router_id') +
                 Suppress(Literal('(Link Data) Router Interface address:')) +
                 ipv4Address('interface_address'))

lsaLinkTransit = (Suppress(Literal('(Link ID) Designated Router address:')) +
                  ipv4Address('router_address') +
                  Suppress(Literal('(Link Data) Router Interface address:')) +
                  ipv4Address('interface_address'))

lsaLink = Group(Suppress(Literal('Link connected to:')) +
                SkipTo(LineEnd())('link_connected_to') +
                (lsaLinkStub ^
                 lsaLinkRouter ^
                 lsaLinkTransit) +
                Suppress(Literal('Number of TOS metrics:')) +
                Word(nums)('number_of_metrics') +
                Suppress(Literal('TOS')) +
                Word(nums)('TOS') +
                Suppress(Literal('Metric:')) +
                Word(nums)('metric'))

router_lsa = Group(lsaAge +
                   lsaOptions +
                   lsaFlags +
                   lsaType +
                   lsaId +
                   lsaAdvRouter +
                   lsaSeqNum +
                   lsaCheksum +
                   lsaLength +
                   lsaNumberOfL +
                   OneOrMore(lsaLink))('router_lsa')

network_lsa = Group(lsaAge +
                    lsaOptions +
                    lsaType +
                    lsaId +
                    lsaAdvRouter +
                    lsaSeqNum +
                    lsaCheksum +
                    lsaLength +
                    lsaNetworkM +
                    OneOrMore(lsaAttRouter))('network_lsa')

summary_lsa = Group(lsaAge +
                    lsaOptions +
                    lsaType +
                    lsaId +
                    lsaAdvRouter +
                    lsaSeqNum +
                    lsaCheksum +
                    lsaLength +
                    lsaNetworkM +
                    lsaTosMetric)('summary_lsa')

external_lsa  = Group(lsaAge +
                      lsaOptions +
                      lsaType +
                      lsaId +
                      lsaAdvRouter +
                      lsaSeqNum +
                      lsaCheksum +
                      lsaLength +
                      lsaNetworkM +
                      lsaMetricType +
                      lsaTOS +
                      lsaMetric +
                      lsaFwdAddres +
                      lsaRouteTag)('external_lsa')

# Header displaying OSPF router ID and process ID
ospfRouterIdWithProcess = (Suppress(Literal('OSPF Router with ID')) +
                           Suppress(Literal('(')) +
                           ipv4Address('router_id') +
                           Suppress(Literal(')')) +
                           Suppress(Literal('(Process ID')) +
                           Word(nums)('process_id') +
                           Suppress(Literal(')')))

externalLSAHeader = Group(Optional(ospfRouterIdWithProcess) +
                          Suppress(Literal('AS External Link States')))('process_info')

routerLSAHeader = Group(Optional(ospfRouterIdWithProcess) +
                        Suppress(Literal('Router Link States (Area')) +
                        ipv4Address('area') +
                        Suppress(Literal(')')))

summaryLSAHeader = Group(Optional(ospfRouterIdWithProcess) +
                         Suppress(Literal('Summary Link States (Area')) +
                         ipv4Address('area') +
                         Suppress(Literal(')')))

networkLSAHeader = Group(Optional(ospfRouterIdWithProcess) +
                         Suppress(Literal('Net Link States (Area')) +
                         ipv4Address('area') +
                         Suppress(Literal(')')))


routerLSA = OneOrMore(Group(routerLSAHeader +
                            OneOrMore(router_lsa)('lsas')))
networkLSA = OneOrMore(Group(networkLSAHeader +
                             OneOrMore(network_lsa)('lsas')))
summaryLSA = OneOrMore(Group(summaryLSAHeader +
                             OneOrMore(summary_lsa)('lsas')))
externalLSA =  OneOrMore(Group(externalLSAHeader +
                               OneOrMore(external_lsa)('lsas')))
