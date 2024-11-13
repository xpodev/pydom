from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGMaskElement
from ..types import ChildType


class Mask(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGMaskElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "mask"
