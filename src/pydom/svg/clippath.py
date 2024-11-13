from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGClipPathElement
from ..types import ChildType


class ClipPath(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGClipPathElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "clippath"
