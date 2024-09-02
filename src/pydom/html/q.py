from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLQuoteElement
from ..types import ChildType


class Q(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLQuoteElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "q"
