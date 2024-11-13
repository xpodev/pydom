from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGTextElement
from ..types import ChildType


class Text(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGTextElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "text"
