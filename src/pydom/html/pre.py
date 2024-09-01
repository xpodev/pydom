from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLPreElement
from ..types import ChildType


class Pre(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLPreElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "pre"
