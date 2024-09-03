from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLBodyElement
from ..types import ChildType


class Body(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLBodyElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "body"
