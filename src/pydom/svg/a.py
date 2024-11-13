from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGAnchorElement
from ..types import ChildType


class A(Element):
    """
    The SVG <a> element provides a way to create hyperlinks within SVG content. It supports any SVG element or graphics element.

    :Notice: The SVG <a> element is not the same as the HTML <a> element. The SVG <a> element is a container for graphics, while the HTML <a> element is a hypertext link.
    """
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGAnchorElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "a"
