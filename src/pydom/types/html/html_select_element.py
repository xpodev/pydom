from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLSelectElement(HTMLElementProps, total=False):
    auto_complete: Optional[str]
    auto_focus: Optional[str]
    disabled: Optional[bool]
    form: Optional[str]
    multiple: Optional[str]
    name: Optional[str]
    required: Optional[str]
    size: Optional[str]
