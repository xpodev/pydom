from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTitleElement
from ..types import ChildType


class Title(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTitleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "title"
