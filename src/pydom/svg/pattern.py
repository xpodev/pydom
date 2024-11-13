from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGPatternElement
from ..types import ChildType


class Pattern(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGPatternElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "pattern"
