from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableColElement
from ..types import ChildType


class Col(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableColElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "col"
    inline = True
