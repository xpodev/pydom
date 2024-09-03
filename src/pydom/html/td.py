from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableDataCellElement
from ..types import ChildType


class Td(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableDataCellElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "td"
