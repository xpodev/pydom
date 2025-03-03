pydom.types.rendering
=====================

.. py:module:: pydom.types.rendering


Attributes
----------

.. autoapisummary::

   pydom.types.rendering.Primitive
   pydom.types.rendering.Renderable
   pydom.types.rendering.ChildType
   pydom.types.rendering.RenderResult
   pydom.types.rendering.ChildrenType
   pydom.types.rendering.RenderTarget


Classes
-------

.. autoapisummary::

   pydom.types.rendering.RenderResultJSON


Module Contents
---------------

.. py:data:: Primitive
   :type:  typing_extensions.TypeAlias

.. py:data:: Renderable
   :type:  typing_extensions.TypeAlias

.. py:data:: ChildType
   :type:  typing_extensions.TypeAlias

.. py:data:: RenderResult
   :type:  typing_extensions.TypeAlias

.. py:data:: ChildrenType
   :type:  typing_extensions.TypeAlias

.. py:data:: RenderTarget
   :type:  typing_extensions.TypeAlias

.. py:class:: RenderResultJSON

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: type
      :type:  str


   .. py:attribute:: props
      :type:  Dict[str, Primitive]


   .. py:attribute:: children
      :type:  List[RenderResultJSON]


