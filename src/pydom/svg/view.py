from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGViewElement
from ..types import ChildType


class View(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGViewElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "view"
