from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.ip.route import ipRoute
import pytest


ipRouteParser = ipRoute + stringEnd