pydom.rendering.transformers.property_transformer
=================================================

.. py:module:: pydom.rendering.transformers.property_transformer


Functions
---------

.. autoapisummary::

   pydom.rendering.transformers.property_transformer.property_transformer


Module Contents
---------------

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



