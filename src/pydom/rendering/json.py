from typing import Optional

from ..context import Context, get_context
from ..errors import RenderError
from .render_state import RenderState
from .tree import build_tree, TreeNode, TextNode, ElementNode
from ..types import RenderResult


def render_json(
    element: RenderResult,
    *,
    context: Optional[Context] = None,
    **render_state_data,
):
    context = get_context(context)
    render_state = RenderState(root=element, render_target="json", **render_state_data)
    context.injector.add(RenderState, render_state)

    tree = build_tree(element, context=context)

    return _render_json(tree)


def _render_json(node: TreeNode):
    if isinstance(node, TextNode):
        return node.text

    if not isinstance(node, ElementNode):
        raise RenderError("Invalid node type")

    children = []
    if node.children is not None:
        for child in node.children:
            children.append(_render_json(child))

    return {
        "type": node.tag_name,
        "props": node.props,
        "children": children,
    }
