from pydom.types.html.aria_props import AriaProps
from pydom.types.html.html_element import HTMLElement
from pydom.types.html.html_event_props import HTMLEventProps


class HTMLElementProps(HTMLElement, AriaProps, HTMLEventProps):
    pass
