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

from pyparsing import (OneOrMore, Word, Group, Optional, printables)
from ...common import (ipv4Prefix, ipv4Address, naturalNumber, suppressedKeyword,
                       interfaceName, ipv4AddressNetwork)

ipRouteTag = (suppressedKeyword('tag') +
              naturalNumber('tag'))
ipRouteDescription = (suppressedKeyword('description') +
                      Word(printables))
ipRouteOptions = OneOrMore(naturalNumber('distance') ^
                           ipRouteDescription('description') ^
                           ipRouteTag('tag'))
ipRouteGateway = (ipv4Address('address') ^
                  interfaceName('interface'))
ipRouteDestination = (ipv4Prefix('prefix') ^
                      ipv4AddressNetwork('network'))
ipRoute = Group(suppressedKeyword('ip') +
                suppressedKeyword('route') +
                ipRouteDestination('destination') +
                Group(ipRouteGateway)('gateway') +
                Optional(ipRouteOptions))('route')
