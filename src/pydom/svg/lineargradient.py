from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGLinearGradientElement
from ..types import ChildType


class LinearGradient(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGLinearGradientElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "lineargradient"
