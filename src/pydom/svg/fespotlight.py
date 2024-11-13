from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFESpotLightElement
from ..types import ChildType


class FeSpotLight(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFESpotLightElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fespotlight"
