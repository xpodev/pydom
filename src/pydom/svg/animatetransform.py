from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGAnimateTransformElement
from ..types import ChildType


class AnimateTransform(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGAnimateTransformElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "animatetransform"
