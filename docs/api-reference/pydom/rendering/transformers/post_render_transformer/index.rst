pydom.rendering.transformers.post_render_transformer
====================================================

.. py:module:: pydom.rendering.transformers.post_render_transformer


Attributes
----------

.. autoapisummary::

   pydom.rendering.transformers.post_render_transformer.P
   pydom.rendering.transformers.post_render_transformer.PostRenderTransformerFunction


Classes
-------

.. autoapisummary::

   pydom.rendering.transformers.post_render_transformer.PostRenderTransformer


Functions
---------

.. autoapisummary::

   pydom.rendering.transformers.post_render_transformer.post_render_transformer


Module Contents
---------------

.. py:data:: P

.. py:data:: PostRenderTransformerFunction
   :type:  typing_extensions.TypeAlias

.. py:class:: PostRenderTransformer

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: transform(element: pydom.rendering.tree.nodes.ContextNode)
      :abstractmethod:



.. py:function:: post_render_transformer(*, context: Union[pydom.context.Context, None] = None, before: Optional[List[Type[PostRenderTransformer]]] = None, after: Optional[List[Type[PostRenderTransformer]]] = None)

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



