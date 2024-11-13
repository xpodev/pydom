from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGSymbolElement
from ..types import ChildType


class Symbol(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGSymbolElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "symbol"
