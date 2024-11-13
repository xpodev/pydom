from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGSVGElement
from ..types import ChildType


class Svg(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGSVGElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "svg"
