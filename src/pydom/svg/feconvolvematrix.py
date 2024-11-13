from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEConvolveMatrixElement
from ..types import ChildType


class FeConvolveMatrix(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEConvolveMatrixElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feconvolvematrix"
