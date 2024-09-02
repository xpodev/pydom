from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLSpanElement
from ..types import ChildType


class Span(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSpanElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "span"
