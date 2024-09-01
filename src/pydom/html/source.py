from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLSourceElement
from ..types import ChildType


class Source(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSourceElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "source"
    inline = True
