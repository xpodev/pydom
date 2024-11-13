from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEPointLightElement
from ..types import ChildType


class FePointLight(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEPointLightElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fepointlight"
