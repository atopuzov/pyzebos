from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.router.ospf import routerOSPF
import pytest


routerOspfParser = routerOSPF + stringEnd