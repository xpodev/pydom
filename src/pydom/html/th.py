from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableHeaderCellElement
from ..types import ChildType


class Th(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableHeaderCellElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "th"
