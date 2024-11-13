from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGEllipseElement
from ..types import ChildType


class Ellipse(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGEllipseElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "ellipse"
