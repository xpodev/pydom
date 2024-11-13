from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGMPathElement
from ..types import ChildType


class MPath(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGMPathElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "mpath"
