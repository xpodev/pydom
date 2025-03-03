pydom.component
===============

.. py:module:: pydom.component


Classes
-------

.. autoapisummary::

   pydom.component.Component


Module Contents
---------------

.. py:class:: Component(*children: pydom.types.rendering.ChildType)

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: children
      :type:  Tuple[pydom.types.rendering.ChildType, Ellipsis]


   .. py:method:: render(*_, **kwargs) -> pydom.types.rendering.RenderResult
      :abstractmethod:



   .. py:method:: __init_subclass__(**kwargs) -> None
      :classmethod:



   .. py:method:: __call__(*children: pydom.types.rendering.ChildType)


