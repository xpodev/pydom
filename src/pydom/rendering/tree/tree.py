from html import escape
from typing import Union, TYPE_CHECKING

from ...component import Component
from ...element import Element
from ...errors import RenderError
from .nodes.context_node import ContextNode
from .nodes import TreeNode, ElementNode, TextNode
from ..props import transform_props
from ...types import Primitive, Renderable
from ...utils.functions import flatten, is_primitive

if TYPE_CHECKING:
    from ...context import Context


def build_raw_tree(
    renderable: Union[Renderable, Primitive], *, context: "Context", escape_string=True
) -> TreeNode:
    while isinstance(renderable, Component):
        renderable = renderable.render()

    if is_primitive(renderable):
        text = str(renderable) if renderable is not None else ""
        if escape_string:
            text = escape(text)
        return TextNode(text)

    if not isinstance(renderable, Element):
        raise RenderError(f"Invalid renderable type: {type(renderable)}")

    children = (
        [
            build_raw_tree(
                child, context=context, escape_string=renderable.escape_children
            )
            for child in flatten(renderable.children)
        ]
        if not renderable.inline
        else None
    )
    element = ElementNode(
        tag_name=renderable.tag_name, props=renderable.props, children=children
    )

    transform_props(ContextNode(element, context=context), context=context)

    return element


def build_tree(
    renderable: Union[Renderable, Primitive], *, context: "Context"
) -> TreeNode:
    tree = build_raw_tree(renderable, context=context)

    if not isinstance(tree, ElementNode):
        return tree

    for transformer in context.post_render_transformers:
        transformer(ContextNode(tree, context=context))

    return tree
