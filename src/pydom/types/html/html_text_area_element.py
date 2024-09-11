from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTextAreaElement(HTMLElementProps, total=False):
    auto_complete: Optional[str]
    auto_focus: Optional[str]
    cols: Optional[str]
    dirname: Optional[str]
    disabled: Optional[bool]
    form: Optional[str]
    max_length: Optional[str]
    min_length: Optional[str]
    name: Optional[str]
    placeholder: Optional[str]
    readonly: Optional[str]
    required: Optional[str]
    rows: Optional[str]
    wrap: Optional[str]
