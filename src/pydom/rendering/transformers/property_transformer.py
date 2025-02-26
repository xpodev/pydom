from typing import Any, Callable, Union, Optional
from ...context.context import PropertyTransformerFunction, Context, get_context


def property_transformer(
    matcher: Union[Callable[[str, Any], bool], str], context: Optional[Context] = None
):
    """
    A decorator to register a function as a property transformer.

    Args:
        matcher: A callable that takes a key and a value and returns a boolean
        indicating whether the transformer should be applied.
        If a string is provided, it is assumed to be a key that should be matched exactly.
        context: The context to register the transformer in. If not provided, the default context is used.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @property_transformer("class_name")
        ... def class_name_mapper(key, value, element):
        ...     if isinstance(class_name, list):
        ...         class_name = " ".join(class_name)
        ...
        ...     element.props["class"] = " ".join(str(class_name).split())

    """
    context = get_context(context)

    def decorator(func: PropertyTransformerFunction):
        context.add_prop_transformer(matcher, func)
        return func

    return decorator
