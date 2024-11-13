from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEDistantLightElement
from ..types import ChildType


class FeDistantLight(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEDistantLightElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fedistantlight"
