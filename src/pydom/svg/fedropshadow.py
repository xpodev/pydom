from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEDropShadowElement
from ..types import ChildType


class FeDropShadow(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEDropShadowElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fedropshadow"
