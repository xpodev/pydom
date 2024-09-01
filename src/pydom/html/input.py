from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLInputElement
from ..types import ChildType


class Input(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLInputElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "input"
    inline = True
