from typing import Literal, Optional
from pydom.types.html.html_element_props import HTMLElementProps


InputType = Literal[
    "button",
    "checkbox",
    "color",
    "date",
    "datetime-local",
    "email",
    "file",
    "hidden",
    "image",
    "month",
    "number",
    "password",
    "radio",
    "range",
    "reset",
    "search",
    "submit",
    "tel",
    "text",
    "time",
    "url",
    "week",
]


class HTMLInputElement(HTMLElementProps, total=False):
    accept: Optional[str]
    alpha: Optional[bool]
    alt: Optional[str]
    auto_capitalize: Optional[str]
    auto_complete: Optional[str]
    auto_focus: Optional[bool]
    capture: Optional[str]
    checked: Optional[bool]
    color_space: Optional[str]
    dirname: Optional[str]
    disabled: Optional[bool]
    form: Optional[str]
    form_action: Optional[str]
    form_enctype: Optional[str]
    form_method: Optional[str]
    form_no_validate: Optional[str]
    form_target: Optional[str]
    height: Optional[str]
    list: Optional[str]
    max: Optional[str]
    max_length: Optional[str]
    min: Optional[str]
    min_length: Optional[str]
    multiple: Optional[str]
    name: Optional[str]
    pattern: Optional[str]
    placeholder: Optional[str]
    popover_target: Optional[str]
    popover_target_action: Optional[str]
    readonly: Optional[bool]
    required: Optional[bool]
    size: Optional[str]
    src: Optional[str]
    step: Optional[str]
    type: Optional[InputType]
    value: Optional[str]
    width: Optional[str]
