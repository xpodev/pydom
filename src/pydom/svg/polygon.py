from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGPolygonElement
from ..types import ChildType


class Polygon(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGPolygonElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "polygon"
