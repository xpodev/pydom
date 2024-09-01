from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLButtonElement
from ..types import ChildType


class Button(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLButtonElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "button"
