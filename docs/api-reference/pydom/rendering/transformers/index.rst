pydom.rendering.transformers
============================

.. py:module:: pydom.rendering.transformers


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/rendering/transformers/post_render_transformer/index
   /api-reference/pydom/rendering/transformers/property_transformer/index


Functions
---------

.. autoapisummary::

   pydom.rendering.transformers.post_render_transformer
   pydom.rendering.transformers.property_transformer


Package Contents
----------------

.. py:function:: post_render_transformer(*, context: Union[pydom.context.context.Context, None] = None, before: Optional[List[Type[pydom.context.transformers.PostRenderTransformer]]] = None, after: Optional[List[Type[pydom.context.transformers.PostRenderTransformer]]] = None)

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



.. py:function:: property_transformer(matcher: Union[Callable[[str, Any], bool], str], *, context: Optional[pydom.context.context.Context] = None, before: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None)

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



