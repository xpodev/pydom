pydom.rendering.transformers.property_transformer
=================================================

.. py:module:: pydom.rendering.transformers.property_transformer


Attributes
----------

.. autoapisummary::

   pydom.rendering.transformers.property_transformer.P
   pydom.rendering.transformers.property_transformer.PropertyMatcherFunction
   pydom.rendering.transformers.property_transformer.PropertyTransformerFunction


Classes
-------

.. autoapisummary::

   pydom.rendering.transformers.property_transformer.PropertyTransformer


Functions
---------

.. autoapisummary::

   pydom.rendering.transformers.property_transformer.property_transformer


Module Contents
---------------

.. py:data:: P

.. py:data:: PropertyMatcherFunction
   :type:  typing_extensions.TypeAlias

.. py:data:: PropertyTransformerFunction
   :type:  typing_extensions.TypeAlias

.. py:class:: PropertyTransformer

   Bases: :py:obj:`abc.ABC`, :py:obj:`Tuple`\ [\ :py:obj:`PropertyMatcherFunction`\ , :py:obj:`PropertyTransformerFunction`\ ]


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: match(prop_name: str, prop_value, /) -> bool
      :abstractmethod:



   .. py:method:: transform(prop_name: str, prop_value, element: pydom.rendering.tree.nodes.ContextNode, /)
      :abstractmethod:



.. py:function:: property_transformer(matcher: Union[Callable[[str, Any], bool], str], *, context: Optional[pydom.context.Context] = None, before: Optional[List[Type[PropertyTransformer]]] = None, after: Optional[List[Type[PropertyTransformer]]] = None)

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



