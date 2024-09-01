from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLOptionElement
from ..types import ChildType


class Option(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOptionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "option"
