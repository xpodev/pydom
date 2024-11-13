from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGScriptElement
from ..types import ChildType


class Script(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGScriptElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "script"
