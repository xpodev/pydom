from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLScriptElement


class Script(Element):
    def __init__(self, *children: str, **kwargs: Unpack["HTMLScriptElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "script"
    escape_children = False
