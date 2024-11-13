from typing import Union

from ...context.context import PostRenderTransformerFunction, get_context, Context


def post_render_transformer(context: Union[Context, None] = None):
    """
    A decorator to register a post-render transformer.

    Post-render transformers are functions that take the rendered tree and can modify it in place.

    Args:
        context: The context to register the transformer with.

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
        context.add_post_render_transformer(func)
        return func

    return decorator
