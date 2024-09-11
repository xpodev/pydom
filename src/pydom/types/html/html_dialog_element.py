from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLDialogElement(HTMLElementProps, total=False):
    open: Optional[str]
