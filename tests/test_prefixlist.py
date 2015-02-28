from pyparsing import stringEnd, ParseException
from pyzebos.parsers.config.prefixlist import prefixList
import pytest


prefixListParser = prefixList + stringEnd
