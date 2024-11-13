from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGAnimateElement
from ..types import ChildType


class Animate(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGAnimateElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "animate"
