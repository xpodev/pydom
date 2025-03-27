pydom.context.context
=====================

.. py:module:: pydom.context.context


Classes
-------

.. autoapisummary::

   pydom.context.context.Context


Functions
---------

.. autoapisummary::

   pydom.context.context.get_context
   pydom.context.context.set_default_context


Module Contents
---------------

.. py:class:: Context

   .. py:attribute:: injector
      :type:  pydom.utils.injector.Injector


   .. py:method:: add_prop_transformer(transformer: pydom.rendering.transformers.PropertyTransformer, /, *, before: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None) -> None
                  add_prop_transformer(matcher: pydom.rendering.transformers.property_transformer.PropertyMatcherFunction, transformer: pydom.rendering.transformers.property_transformer.PropertyTransformerFunction, /, *, before: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None) -> None


   .. py:method:: add_post_render_transformer(transformer: Union[pydom.rendering.transformers.post_render_transformer.PostRenderTransformerFunction, pydom.rendering.transformers.PostRenderTransformer], /, *, before: Optional[List[Type[pydom.rendering.transformers.PostRenderTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PostRenderTransformer]]] = None)


   .. py:property:: prop_transformers


   .. py:property:: post_render_transformers


   .. py:method:: inject(callback: Callable) -> Callable


   .. py:method:: standard() -> typing_extensions.Self
      :classmethod:



.. py:function:: get_context(context: Optional[Context] = None) -> Context

.. py:function:: set_default_context(context: Context) -> None

