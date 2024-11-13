from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFETurbulenceElement
from ..types import ChildType


class FeTurbulence(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFETurbulenceElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feturbulence"
