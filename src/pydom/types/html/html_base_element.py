from pydom.types.html.html_element_props import HTMLElementProps


class HTMLBaseElement(HTMLElementProps, total=False):
    href: str
    target: str
