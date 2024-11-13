from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEFuncGElement
from ..types import ChildType


class FeFuncG(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEFuncGElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fefuncg"
