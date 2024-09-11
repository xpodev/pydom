from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLDocumentMetaElement(HTMLElementProps, total=False):
    name: Optional[str]
    content: Optional[str]
