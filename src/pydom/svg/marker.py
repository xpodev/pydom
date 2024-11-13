from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGMarkerElement
from ..types import ChildType


class Marker(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGMarkerElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "marker"
