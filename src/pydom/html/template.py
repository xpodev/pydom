from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTemplateElement
from ..types import ChildType


class Template(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTemplateElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "template"
