from html import escape
from typing import Any, TYPE_CHECKING, Dict

from ..errors import RenderError

if TYPE_CHECKING:
    from ..context import Context
    from .tree.nodes.context_node import ContextNode


def transform_props(element: "ContextNode", *, context: "Context"):
    for matcher, transformer in context.prop_transformers:
        if isinstance(matcher, str):
            key = matcher
            if key in element.props:
                value = element.props[key]
                if callable(transformer):
                    transformer(key, value, element)
                else:
                    element.props[transformer] = value
        elif callable(matcher):
            for key, value in list(element.props.items()):
                if matcher(key, value):
                    transformer(key, value, element)
        else:
            raise RenderError(f"Invalid matcher: {matcher} must be a callable or a string.")

    element.props.update(element.props)


def render_props(props: Dict[str, Any]) -> str:
    return " ".join(key if value is True else f'{key}="{escape(str(value))}"' for key, value in props.items())
