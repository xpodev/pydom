from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGPathElement
from ..types import ChildType


class Path(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGPathElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "path"
