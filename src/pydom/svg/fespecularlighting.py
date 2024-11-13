from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFESpecularLightingElement
from ..types import ChildType


class FeSpecularLighting(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFESpecularLightingElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fespecularlighting"
