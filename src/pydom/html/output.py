from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLOutputElement
from ..types import ChildType


class Output(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOutputElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "output"
