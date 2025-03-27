pydom.context
=============

.. py:module:: pydom.context


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/context/context/index
   /api-reference/pydom/context/standard/index


Classes
-------

.. autoapisummary::

   pydom.context.Context


Functions
---------

.. autoapisummary::

   pydom.context.get_context


Package Contents
----------------

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

