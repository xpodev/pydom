from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLOutputElement(HTMLElementProps, total=False):
    html_for: Optional[str]  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: Optional[str]
    name: Optional[str]
