from typing import overload, Literal, Union, Optional

from ..context import Context
from .html import render_html
from .json import render_json
from ..types import Renderable, Primitive


@overload
def render(
    element: Union[Renderable, Primitive],
    *,
    to: Literal["html"],
    pretty: bool = False,
    tab_indent: int = 1,
    context: Optional[Context] = None,
    **render_state_data,
) -> str: ...


@overload
def render(
    element: Union[Renderable, Primitive],
    *,
    to: Literal["json"],
    context: Optional[Context] = None,
    **render_state_data,
) -> dict: ...


@overload
def render(
    element: Union[Renderable, Primitive],
    *,
    pretty: bool = False,
    tab_indent: int = 1,
    context: Optional[Context] = None,
    **render_state_data,
) -> str: ...


def render(
    element: Union[Renderable, Primitive],
    *,
    to: Literal["json", "html"] = "html",
    **kwargs,
) -> Union[str, dict]:

    if to == "json":
        return render_json(element, **kwargs)
    if to == "html":
        return render_html(element, **kwargs)


__all__ = ["render", "render_html", "render_json"]