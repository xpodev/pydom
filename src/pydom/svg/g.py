from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGGElement
from ..types import ChildType


class G(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGGElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "g"
