from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEOffsetElement
from ..types import ChildType


class FeOffset(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEOffsetElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feoffset"
