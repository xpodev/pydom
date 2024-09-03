from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLListItemElement
from ..types import ChildType


class Li(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLListItemElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "li"
