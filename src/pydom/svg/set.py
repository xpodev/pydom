from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGSetElement
from ..types import ChildType


class Set(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGSetElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "set"
