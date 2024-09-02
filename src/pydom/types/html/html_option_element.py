from pydom.types.html.html_element_props import HTMLElementProps


class HTMLOptionElement(HTMLElementProps, total=False):
    disabled: bool
    label: str
    selected: str
    value: str
