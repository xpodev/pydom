from typing import List, Optional, Type, Union

from ...context.context import PostRenderTransformerFunction, get_context, Context
from ...context.transformers import PostRenderTransformer


def post_render_transformer(
    *,
    context: Union[Context, None] = None,
    before: Optional[List[Type[PostRenderTransformer]]] = None,
    after: Optional[List[Type[PostRenderTransformer]]] = None,
):
    """
    A decorator to register a function as a post-render transformer.

    Args:
        context: The context to register the transformer with. If not provided, the default context is used.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @post_render_transformer()
        ... def add_custom_script(root: ElementNode):
        ...     root.get_by_tag("head").append_child(
        ...         ElementNode(
        ...             tag_name="script",
        ...             props={"src": "/custom.js"},
        ...         )
        ...     )

    """
    context = get_context(context)

    def decorator(func: PostRenderTransformerFunction):
        context.add_post_render_transformer(func, before=before, after=after)
        return func

    return decorator
