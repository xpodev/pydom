from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGDescElement
from ..types import ChildType


class Desc(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGDescElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "desc"
