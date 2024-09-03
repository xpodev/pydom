from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLDivElement
from ..types import ChildType


class Div(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDivElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "div"
