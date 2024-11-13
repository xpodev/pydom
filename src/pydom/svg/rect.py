from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGRectElement
from ..types import ChildType


class Rect(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGRectElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "rect"
