from typing import Union

from ...component import Component
from ...context import Context
from ...element import Element
from ...errors import RenderError
from .nodes.context_node import ContextNode
from .nodes import TreeNode, ElementNode, TextNode
from ..props import transform_props
from ...types import Primitive, Renderable
from ...utils.functions import is_primitive


def build_raw_tree(
    renderable: Union[Renderable, Primitive], *, context: "Context"
) -> TreeNode:
    while isinstance(renderable, Component):
        renderable = renderable.render()

    if is_primitive(renderable):
        return TextNode(renderable)

    if not isinstance(renderable, Element):
        raise RenderError(f"Invalid renderable type: {type(renderable)}")

    children = (
        [build_raw_tree(child, context=context) for child in renderable.children]
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
