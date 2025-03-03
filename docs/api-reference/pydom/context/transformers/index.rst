pydom.context.transformers
==========================

.. py:module:: pydom.context.transformers


Attributes
----------

.. autoapisummary::

   pydom.context.transformers.T
   pydom.context.transformers.P
   pydom.context.transformers.PropertyMatcherFunction
   pydom.context.transformers.PropertyTransformerFunction
   pydom.context.transformers.PostRenderTransformerFunction


Classes
-------

.. autoapisummary::

   pydom.context.transformers.PropertyTransformer
   pydom.context.transformers.PostRenderTransformer


Module Contents
---------------

.. py:data:: T

.. py:data:: P

.. py:data:: PropertyMatcherFunction
   :type:  typing_extensions.TypeAlias

.. py:data:: PropertyTransformerFunction
   :type:  typing_extensions.TypeAlias

.. py:data:: PostRenderTransformerFunction
   :type:  typing_extensions.TypeAlias

.. py:class:: PropertyTransformer

   Bases: :py:obj:`abc.ABC`, :py:obj:`Tuple`\ [\ :py:obj:`PropertyMatcherFunction`\ , :py:obj:`PropertyTransformerFunction`\ ]


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: match(prop_name: str, prop_value, /) -> bool
      :abstractmethod:



   .. py:method:: transform(prop_name: str, prop_value, element: pydom.rendering.tree.nodes.ContextNode, /)
      :abstractmethod:



.. py:class:: PostRenderTransformer

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: transform(element: pydom.rendering.tree.nodes.ContextNode)
      :abstractmethod:



