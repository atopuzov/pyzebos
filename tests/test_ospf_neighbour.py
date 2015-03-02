from pyparsing import stringEnd, ParseException
from pyzebos.parsers.show.ospf_neighbour import ospfNeighbour
import pytest


ospfNeighbourParser = ospfNeighbour + stringEnd
