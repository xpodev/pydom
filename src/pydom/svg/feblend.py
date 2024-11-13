from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEBlendElement
from ..types import ChildType


class FeBlend(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEBlendElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feblend"
