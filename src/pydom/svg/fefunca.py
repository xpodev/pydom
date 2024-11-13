from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEFuncAElement
from ..types import ChildType


class FeFuncA(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEFuncAElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fefunca"
