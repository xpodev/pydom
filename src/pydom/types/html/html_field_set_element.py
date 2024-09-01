from pydom.types.html.html_element_props import HTMLElementProps


class HTMLFieldSetElement(HTMLElementProps, total=False):
    disabled: str
    form: str
    name: str
