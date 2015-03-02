from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_database import routerLSA, networkLSA, summaryLSA, externalLSA
import pytest


routerLSAParser = routerLSA + stringEnd
networkLSAParser = networkLSA + stringEnd
summaryLSAParser = summaryLSA + stringEnd
externalLSAParser = externalLSA + stringEnd
