from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.router.bgp import routerBGP
import pytest


routerBgpParser = routerBGP + stringEnd