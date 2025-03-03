pydom.context.context
=====================

.. py:module:: pydom.context.context


Attributes
----------

.. autoapisummary::

   pydom.context.context.T
   pydom.context.context.P


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

.. py:data:: T

.. py:data:: P

.. py:class:: Context

   .. py:attribute:: injector
      :type:  pydom.utils.injector.Injector


   .. py:method:: add_prop_transformer(transformer: pydom.context.transformers.PropertyTransformer, /, *, before: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None) -> None
                  add_prop_transformer(matcher: pydom.context.transformers.PropertyMatcherFunction, transformer: pydom.context.transformers.PropertyTransformerFunction, /, *, before: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.context.transformers.PropertyTransformer]]] = None) -> None


   .. py:method:: add_post_render_transformer(transformer: Union[pydom.context.transformers.PostRenderTransformerFunction, pydom.context.transformers.PostRenderTransformer], /, *, before: Optional[List[Type[pydom.context.transformers.PostRenderTransformer]]] = None, after: Optional[List[Type[pydom.context.transformers.PostRenderTransformer]]] = None)


   .. py:property:: prop_transformers


   .. py:property:: post_render_transformers


   .. py:method:: inject(callback: Callable) -> Callable


   .. py:method:: standard() -> typing_extensions.Self
      :classmethod:



.. py:function:: get_context(context: Optional[Context] = None) -> Context

.. py:function:: set_default_context(context: Context) -> None

