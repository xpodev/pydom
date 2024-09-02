from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLDetailsElement
from ..types import ChildType


class Details(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDetailsElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "details"
