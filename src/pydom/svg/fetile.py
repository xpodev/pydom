from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFETileElement
from ..types import ChildType


class FeTile(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFETileElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fetile"
