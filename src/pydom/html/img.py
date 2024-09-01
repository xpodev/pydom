from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLImageElement
from ..types import ChildType


class Img(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLImageElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "img"
    inline = True
