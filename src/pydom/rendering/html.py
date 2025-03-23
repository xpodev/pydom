from typing import Optional, TYPE_CHECKING

from ..errors import RenderError
from .props import render_props
from .render_state import RenderState
from .tree import ElementNode, TreeNode, TextNode, build_tree
from ..types import RenderResult

if TYPE_CHECKING:
    from ..context import Context


def render_html(
    element: RenderResult,
    *,
    context: Optional["Context"] = None,
    pretty=False,
    tab_indent=1,
    **render_state_data,
) -> str:
    """
    Renders the given element into an HTML string.

    Args:
        element (Renderable | Primitive): The element to be rendered.
        pretty (bool, optional): Whether to format the HTML string with indentation and line breaks. Defaults to False.
        tab_indent (int, optional): The number of spaces to use for indentation when pretty is True. Defaults to 1.

    Returns:
        str: The rendered HTML string.
    """
    from ..context import get_context

    context = get_context(context)
    render_state = RenderState(root=element, render_target="html", **render_state_data)
    with context.injector.scope({RenderState: lambda: render_state}):
        tree = build_tree(element, context=context)

    return _render_html(tree, pretty=pretty, tab_indent=tab_indent)


def _render_html(node: TreeNode, pretty=False, tab_indent=0):
    tab = "  " * tab_indent if pretty else ""
    newline = "\n" if pretty else ""

    if isinstance(node, TextNode):
        return tab + node.text

    if not isinstance(node, ElementNode):
        raise RenderError("Invalid node type")

    props_string = render_props(node.props)
    open_tag = f"{node.tag_name} {props_string}".strip()

    if node.children is None:
        return tab + f"<{open_tag} />"

    children = newline.join(
        _render_html(child, pretty=pretty, tab_indent=tab_indent + 1)
        for child in node.children
    )

    if not node.tag_name:
        return tab + children

    return (
        tab + f"<{open_tag}>{newline if children else ''}{children}</{node.tag_name}>"
    )
