from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLDialogElement
from ..types import ChildType


class Dialog(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDialogElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "dialog"
