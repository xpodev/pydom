from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGTextPathElement
from ..types import ChildType


class TextPath(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGTextPathElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "textpath"
