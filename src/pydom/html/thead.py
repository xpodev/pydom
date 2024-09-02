from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableSectionElement
from ..types import ChildType


class THead(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableSectionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "thead"
