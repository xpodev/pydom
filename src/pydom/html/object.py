from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLObjectElement
from ..types import ChildType


class Object(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLObjectElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "object"
