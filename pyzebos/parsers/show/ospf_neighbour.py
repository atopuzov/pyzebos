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

from pyparsing import (Group, Combine, Suppress, OneOrMore,
                       Literal, Word, alphanums, alphas, nums)
from ..common import ipv4Address, timestamp


ospfState = Combine(Literal('Full') +
                    Literal('/') +
                    (Literal('DR') ^
                     Literal(' -')))

ospfState = (Word(alphas)('state') +
             Suppress(Literal('/')) +
             Word(alphas + '-')('state_dr'))

ospfNeighbourStart = (Suppress(Literal('OSPF process')) +
                      Word(nums)('process_id') +
                      Suppress(Literal(':')))

ospfNeighbourTableHeader = Suppress(Literal('Neighbor ID') +
                                    Literal('Pri') +
                                    Literal('State') +
                                    Literal('Dead Time') +
                                    Literal('Address') +
                                    Literal('Interface'))

ospfNeighbourTableRow = Group(ipv4Address('neighbour_id') +
                              Word(nums)('priority') +
                              ospfState('state') +
                              timestamp('dead_time') +
                              ipv4Address('address') +
                              Word(alphanums)('interface'))('neighbour')

ospfNeighbour = Group(ospfNeighbourStart +
                      ospfNeighbourTableHeader +
                      OneOrMore(ospfNeighbourTableRow)('neighbours'))('process')
