from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFilterElement
from ..types import ChildType


class Filter(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFilterElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "filter"
