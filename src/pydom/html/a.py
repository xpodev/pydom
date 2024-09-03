from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLAnchorElement
from ..types import ChildType


class A(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLAnchorElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "a"
