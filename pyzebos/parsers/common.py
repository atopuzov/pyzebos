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

from pyparsing import (Combine, Suppress, SkipTo, LineEnd, Literal, Word, nums,
                       alphanums, printables, hexnums, Group, Optional, OneOrMore,
                       Keyword)


# IP Address
simpleIpAddress = Combine(Word(nums) + ('.' + Word(nums))*3)

# IPv4 Address
LeadingZeros = Optional(Literal('0'))
octet = Combine((OneOrMore(Literal('0'))) ^
                (LeadingZeros        + Word('123456789', exact = 1)) ^
                (LeadingZeros        + Word('123456789', '0123456789', exact = 2)) ^
                (LeadingZeros + '1'  + Word('0123456789', exact = 2)) ^
                (LeadingZeros + '2'  + Word('01234', '0123456789', exact = 2)) ^
                (LeadingZeros + '25' + Word('012345', exact = 1)))
ipv4Address = Combine(octet + ('.' + octet) * 3)

# IPv6 Address
# http://tools.ietf.org/html/rfc3986#appendix-A
Colon = Literal(':')
DoubleColon = Literal('::')
h16 = Word(hexnums, min=1, max=4)
G = Word(hexnums, min=1, max=4)
ls32 = ((h16 + Colon + h16) ^ ipv4Address)

ipv6Address = Combine(
    (                                        (h16 + Colon) * 6 + ls32) ^
    (                          DoubleColon + (h16 + Colon) * 5 + ls32) ^
    (                    h16 + DoubleColon + (h16 + Colon) * 4 + ls32) ^
    (                          DoubleColon + (h16 + Colon) * 4 + ls32) ^
    ( h16 + Colon      + h16 + DoubleColon + (h16 + Colon) * 3 + ls32) ^
    (                    h16 + DoubleColon + (h16 + Colon) * 3 + ls32) ^
    (                          DoubleColon + (h16 + Colon) * 3 + ls32) ^
    (                    h16 + DoubleColon + (h16 + Colon) * 2 + ls32) ^
    ( h16 + Colon      + h16 + DoubleColon + (h16 + Colon) * 2 + ls32) ^
    ((h16 + Colon) * 2 + h16 + DoubleColon + (h16 + Colon) * 2 + ls32) ^
    (                          DoubleColon + (h16 + Colon) * 2 + ls32) ^
    (                    h16 + DoubleColon +  h16 + Colon      + ls32) ^
    ( h16 + Colon      + h16 + DoubleColon +  h16 + Colon      + ls32) ^
    ((h16 + Colon) * 2 + h16 + DoubleColon +  h16 + Colon      + ls32) ^
    ((h16 + Colon) * 3 + h16 + DoubleColon +  h16 + Colon      + ls32) ^
    (                          DoubleColon +  h16 + Colon      + ls32) ^
    (                    h16 + DoubleColon                     + ls32) ^
    ( h16 + Colon      + h16 + DoubleColon                     + ls32) ^
    ((h16 + Colon) * 2 + h16 + DoubleColon                     + ls32) ^
    ((h16 + Colon) * 3 + h16 + DoubleColon                     + ls32) ^
    ((h16 + Colon) * 4 + h16 + DoubleColon                     + ls32) ^
    (                          DoubleColon                     + ls32) ^
    (                    h16 + DoubleColon                     + h16)  ^
    ( h16 + Colon      + h16 + DoubleColon                     + h16)  ^
    ((h16 + Colon) * 2 + h16 + DoubleColon                     + h16)  ^
    ((h16 + Colon) * 3 + h16 + DoubleColon                     + h16)  ^
    ((h16 + Colon) * 4 + h16 + DoubleColon                     + h16)  ^
    ((h16 + Colon) * 5 + h16 + DoubleColon                     + h16)  ^
    (                          DoubleColon                     + h16)  ^
    (                    h16 + DoubleColon)                            ^
    ( h16 + Colon      + h16 + DoubleColon)                            ^
    ((h16 + Colon) * 2 + h16 + DoubleColon)                            ^
    ((h16 + Colon) * 3 + h16 + DoubleColon)                            ^
    ((h16 + Colon) * 4 + h16 + DoubleColon)                            ^
    ((h16 + Colon) * 5 + h16 + DoubleColon)                            ^
    ((h16 + Colon) * 6 + h16 + DoubleColon)                            ^
    (                          DoubleColon)
)


# IP Prefix
ipv4Prefix =  Group(ipv4Address('network') + Suppress(Literal('/')) + Word(nums)('length'))

ipAddressNetwork = Group(ipv4Address('network') +
                           ipv4Address('netmask'))

# ZebOS comment
zebosComment = Suppress(Literal('!') + SkipTo(LineEnd()))

naturalNumber = Word(nums)

def suppressedKeyword(keyword):
    '''Suppresed (ignored keyword)'''
    return Suppress(Keyword(keyword))

# Access list name
accesslistName = Word(alphanums + '-')

# Interface name
interfaceName = Word(printables)

# route-map name
routeMapName = Word(printables)

timestamp = Group(Word(nums, max=2)('hours') + \
                  Suppress(Literal(':')) + \
                  Word(nums, max=2)('minutes') + \
                  Suppress(Literal(':')) + \
                  Word(nums, max=2)('seconds'))
