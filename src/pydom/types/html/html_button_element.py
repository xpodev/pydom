from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLButtonElement(HTMLElementProps, total=False):
    auto_focus: Optional[str]
    disabled: Optional[bool]
    form: Optional[str]
    form_action: Optional[str]
    form_enctype: Optional[str]
    form_method: Optional[str]
    form_no_validate: Optional[str]
    form_target: Optional[str]
    name: Optional[str]
    type: Optional[str]
    value: Optional[str]
