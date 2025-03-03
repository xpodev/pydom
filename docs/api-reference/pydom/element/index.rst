pydom.element
=============

.. py:module:: pydom.element


Attributes
----------

.. autoapisummary::

   pydom.element.PropsType


Classes
-------

.. autoapisummary::

   pydom.element.Element


Module Contents
---------------

.. py:data:: PropsType

.. py:class:: Element(*args: pydom.types.rendering.ChildType, children: Optional[pydom.types.rendering.ChildrenType] = None, **kwargs: typing_extensions.Unpack[PropsType])

   Bases: :py:obj:`Generic`\ [\ :py:obj:`PropsType`\ ]


   .. py:attribute:: children


   .. py:attribute:: props


   .. py:attribute:: tag_name
      :type:  str


   .. py:attribute:: inline
      :value: False



   .. py:attribute:: escape_children
      :value: True



   .. py:method:: __call__(*children: pydom.types.rendering.ChildType)


