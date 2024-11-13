from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEDiffuseLightingElement
from ..types import ChildType


class FeDiffuseLighting(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEDiffuseLightingElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fediffuselighting"
