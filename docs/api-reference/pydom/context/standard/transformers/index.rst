pydom.context.standard.transformers
===================================

.. py:module:: pydom.context.standard.transformers


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/context/standard/transformers/class_transformer/index
   /api-reference/pydom/context/standard/transformers/dash_transformer/index
   /api-reference/pydom/context/standard/transformers/falsy_transformer/index
   /api-reference/pydom/context/standard/transformers/html_events_transformer/index
   /api-reference/pydom/context/standard/transformers/inner_html_transformer/index
   /api-reference/pydom/context/standard/transformers/simple_transformer/index
   /api-reference/pydom/context/standard/transformers/style_transformer/index


Classes
-------

.. autoapisummary::

   pydom.context.standard.transformers.ClassTransformer
   pydom.context.standard.transformers.DashTransformer
   pydom.context.standard.transformers.FalsyTransformer
   pydom.context.standard.transformers.HTMLEventsTransformer
   pydom.context.standard.transformers.InnerHTMLTransformer
   pydom.context.standard.transformers.SimpleTransformer
   pydom.context.standard.transformers.StyleTransformer


Package Contents
----------------

.. py:class:: ClassTransformer(prop_name='classes')

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:attribute:: prop_name
      :value: 'classes'



   .. py:method:: match(prop_name, _) -> bool


   .. py:method:: transform(_, prop_value, element)


.. py:class:: DashTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(prop_name, _) -> bool


   .. py:method:: transform(_, prop_value, element)


.. py:class:: FalsyTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(_, prop_value) -> bool


   .. py:method:: transform(prop_name, _, element)


.. py:class:: HTMLEventsTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(prop_name, prop_value) -> bool


   .. py:method:: transform(prop_name, prop_value, element)


.. py:class:: InnerHTMLTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(prop_name: str, _) -> bool


   .. py:method:: transform(_, inner_html, element)


.. py:class:: SimpleTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(prop_name, _) -> bool


   .. py:method:: transform(prop_name, _, element)


.. py:class:: StyleTransformer

   Bases: :py:obj:`pydom.rendering.transformers.PropertyTransformer`


   .. py:method:: match(_, value)


   .. py:method:: transform(key: str, value: pydom.styling.StyleSheet, element)


