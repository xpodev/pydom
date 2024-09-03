from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLModElement
from ..types import ChildType


class Del(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLModElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "del"
