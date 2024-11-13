from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGDefsElement
from ..types import ChildType


class Defs(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGDefsElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "defs"
