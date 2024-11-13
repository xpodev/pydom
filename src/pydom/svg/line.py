from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGLineElement
from ..types import ChildType


class Line(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGLineElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "line"
