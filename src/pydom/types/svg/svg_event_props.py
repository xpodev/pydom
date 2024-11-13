from typing_extensions import TypedDict


class SVGEventProps(TypedDict, total=False):
    on_abort: str
    on_error: str
    on_load: str
    on_resize: str
    on_scroll: str
    on_unload: str
