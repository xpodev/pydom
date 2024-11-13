from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGCircleElement
from ..types import ChildType


class Circle(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGCircleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "circle"
