from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGTSpanElement
from ..types import ChildType


class TSpan(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGTSpanElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "tspan"
