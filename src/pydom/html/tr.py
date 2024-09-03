from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableRowElement
from ..types import ChildType


class Tr(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableRowElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "tr"
