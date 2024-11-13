from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGRadialGradientElement
from ..types import ChildType


class RadialGradient(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGRadialGradientElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "radialgradient"
