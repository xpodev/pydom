from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEFuncRElement
from ..types import ChildType


class FeFuncR(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEFuncRElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fefuncr"
