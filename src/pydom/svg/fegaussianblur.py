from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEGaussianBlurElement
from ..types import ChildType


class FeGaussianBlur(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEGaussianBlurElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fegaussianblur"
