from typing_extensions import TypedDict


class ElementProps(TypedDict, total=False, closed=False):
    access_key: str
    auto_capitalize: str
    classes: str
    content_editable: str
    dangerously_set_inner_html: str
    dir: str
    draggable: str
    hidden: str
    id: str
    input_mode: str
    lang: str
    role: str
    spell_check: str
    style: str
    tab_index: str
    title: str
    translate: str

