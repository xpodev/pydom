from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLMeterElement(HTMLElementProps, total=False):
    form: Optional[str]
    high: Optional[str]
    low: Optional[str]
    max: Optional[str]
    min: Optional[str]
    optimum: Optional[str]
    value: Optional[str]
