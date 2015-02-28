from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.accesslist import accessList
import pytest


routerBgpParser = accessList + stringEnd