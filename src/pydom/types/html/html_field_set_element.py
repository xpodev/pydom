from pydom.types.html.html_element_props import HTMLElementProps


class HTMLFieldSetElement(HTMLElementProps, total=False):
    disabled: bool
    form: str
    name: str
