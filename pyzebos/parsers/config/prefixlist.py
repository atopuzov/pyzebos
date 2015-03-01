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

from pyparsing import (Word, Keyword, Optional, Suppress, SkipTo, LineEnd,
                       printables, Group)
from ..common import suppressedKeyword, naturalNumber, ipv4Prefix

action = (Keyword('permit') ^
          Keyword('deny'))
le = (suppressedKeyword('le') +
      naturalNumber)('le')
ge = (suppressedKeyword('ge') +
      naturalNumber)('ge')

ipPrefixPrefix = (ipv4Prefix ^
                  Keyword('any'))
ipPrefixListSeq = (suppressedKeyword('seq') +
                   naturalNumber('seq') +
                   action('action') +
                   ipPrefixPrefix('prefix') +
                   Optional(ge) +
                   Optional(le))

ipPrefixDescription = (suppressedKeyword('description') +
                       SkipTo(LineEnd())('description'))

prefixList = Group((Suppress(Keyword('ip prefix-list')) +
                    Word(printables)('name') +
                    (ipPrefixListSeq ^
                     ipPrefixDescription))('prefix-list'))

# +-ip
#   +-prefix-list
#     +-WORD
#       +-deny
#         +-A.B.C.D/M [ip prefix-list WORD (deny|permit) (A.B.C.D/M|any)]
#           +-ge
#             +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M ge <0-32>]
#               +-le
#                 +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M ge <0-32> le <0-32>]
#           +-le
#             +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M le <0-32>]
#               +-ge
#                 +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M le <0-32> ge <0-32>]
#         +-any [ip prefix-list WORD (deny|permit) (A.B.C.D/M|any)]
#       +-description
#         +-LINE [ip prefix-list WORD description LINE]
#       +-permit
#         +-A.B.C.D/M [ip prefix-list WORD (deny|permit) (A.B.C.D/M|any)]
#           +-ge
#             +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M ge <0-32>]
#               +-le
#                 +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M ge <0-32> le <0-32>]
#           +-le
#             +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M le <0-32>]
#               +-ge
#                 +-<0-32> [ip prefix-list WORD (deny|permit) A.B.C.D/M le <0-32> ge <0-32>]
#         +-any [ip prefix-list WORD (deny|permit) (A.B.C.D/M|any)]
#       +-seq
#         +-<1-4294967295>
#           +-deny
#             +-A.B.C.D/M [ip prefix-list WORD seq <1-4294967295> (deny|permit) (A.B.C.D/M|any)]
#               +-ge
#                 +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M ge <0-32>]
#                   +-le
#                     +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M ge <0-32> le <0-32>]
#               +-le
#                 +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M le <0-32>]
#                   +-ge
#                     +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M le <0-32> ge <0-32>]
#             +-any [ip prefix-list WORD seq <1-4294967295> (deny|permit) (A.B.C.D/M|any)]
#           +-permit
#             +-A.B.C.D/M [ip prefix-list WORD seq <1-4294967295> (deny|permit) (A.B.C.D/M|any)]
#               +-ge
#                 +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M ge <0-32>]
#                   +-le
#                     +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M ge <0-32> le <0-32>]
#               +-le
#                 +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M le <0-32>]
#                   +-ge
#                     +-<0-32> [ip prefix-list WORD seq <1-4294967295> (deny|permit) A.B.C.D/M le <0-32> ge <0-32>]
