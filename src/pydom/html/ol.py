from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLOrderedListElement
from ..types import ChildType


class Ol(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOrderedListElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "ol"
