from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGPolylineElement
from ..types import ChildType


class Polyline(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGPolylineElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "polyline"
