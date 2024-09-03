from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLSlotElement
from ..types import ChildType


class Slot(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSlotElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "slot"
