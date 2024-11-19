from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLStyleElement
from ..types import ChildType


class Style(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLStyleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "style"
    escape_children = False
