from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGTitleElement
from ..types import ChildType


class Title(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGTitleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "title"
