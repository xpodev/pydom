from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEColorMatrixElement
from ..types import ChildType


class FeColorMatrix(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEColorMatrixElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fecolormatrix"
