pydom.context.standard.transformers.class_transformer
=====================================================

.. py:module:: pydom.context.standard.transformers.class_transformer


Classes
-------

.. autoapisummary::

   pydom.context.standard.transformers.class_transformer.ClassTransformer


Module Contents
---------------

.. py:class:: ClassTransformer(prop_name='classes')

   Bases: :py:obj:`pydom.context.transformers.PropertyTransformer`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: prop_name
      :value: 'classes'



   .. py:method:: match(prop_name, _) -> bool


   .. py:method:: transform(_, prop_value, element)


