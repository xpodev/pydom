from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFECompositeElement
from ..types import ChildType


class FeComposite(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFECompositeElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fecomposite"
