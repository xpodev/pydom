from typing import Literal, Optional, Union
from pydom.types.svg.svg_element_props import SVGElementProps


class SVGAnimateElement(SVGElementProps, total=False):
    attribute_name: Optional[str]
    attribute_type: Optional[str]
    dur: Optional[str]
    fill: Optional[str]
    svg_from: Optional[str]
    href: Optional[str]
    repeat_count: Optional[Union[int, Literal["indefinite"]]]
    system_language: Optional[str]
    to: Optional[str]
    values: Optional[str]
