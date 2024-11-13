from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEFuncBElement
from ..types import ChildType


class FeFuncB(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEFuncBElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fefuncb"
