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

from pyparsing import (Group, Suppress, Optional, Keyword, SkipTo, LineEnd)
from ..common import (ipv4Address, ipv4AddressNetwork, ipv4Prefix,
                      suppressedKeyword, naturalNumber, accesslistName)

action = (Keyword('permit') ^
          Keyword('deny'))('action')

ipv4AddressHost = suppressedKeyword('host') + ipv4Address
ipv4AddressAny = Keyword('any')

accessListStart = Suppress(Keyword('access-list'))

# Standard access-list
standardAccessListAddress = (ipv4AddressNetwork ^
                             ipv4AddressHost ^
                             ipv4AddressAny ^
                             ipv4Address)('address')
remarkAction = (Suppress(Keyword('remark') +
                         SkipTo(LineEnd())))
standardAccessListOtherActions = (action +
                                  standardAccessListAddress)
standardAccessListActions = (remarkAction ^
                             standardAccessListOtherActions)
standardAccessList = Group(accessListStart +
                           naturalNumber('number') +
                           standardAccessListActions)('standard')

# Extended access-list
extendedAccessListAddress = (ipv4AddressNetwork ^
                             ipv4AddressHost ^
                             ipv4AddressAny)('address')
extendedAccessListOtherActions = (action +
                                  Suppress(Keyword('ip')) +
                                  extendedAccessListAddress('source') +
                                  extendedAccessListAddress('destination'))
extendedAccessListActions = (remarkAction ^
                             extendedAccessListOtherActions)('action')
extendedAccessList = Group(accessListStart +
                           naturalNumber('number') +
                           extendedAccessListActions)('extended')

# Named access-list
namedAccessListAddress = (ipv4Prefix ^
                          ipv4AddressAny)('address')
namedAccessListOtherActions = (action +
                               namedAccessListAddress +
                               Optional(Keyword('exact-match')))
namedAccessListActions = (remarkAction ^
                          namedAccessListOtherActions)
namedAccessList = Group(accessListStart +
                        accesslistName('name') +
                        namedAccessListActions)('named')

accessList = (standardAccessList ^
              extendedAccessList ^
              namedAccessList)
