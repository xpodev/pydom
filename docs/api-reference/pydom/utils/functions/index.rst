pydom.utils.functions
=====================

.. py:module:: pydom.utils.functions


Attributes
----------

.. autoapisummary::

   pydom.utils.functions.ascii_length


Functions
---------

.. autoapisummary::

   pydom.utils.functions.random_string
   pydom.utils.functions.to_iter
   pydom.utils.functions.is_primitive
   pydom.utils.functions.flatten
   pydom.utils.functions.remove_prefix


Module Contents
---------------

.. py:data:: ascii_length
   :value: 52


.. py:function:: random_string(length=12)

.. py:function:: to_iter(value: typing_extensions.Iterable[_T]) -> typing_extensions.Iterator[_T]
                 to_iter(value: _T) -> typing_extensions.Iterator[_T]

.. py:function:: is_primitive(value) -> typing_extensions.TypeGuard[pydom.types.Primitive]

.. py:function:: flatten(iterable)

.. py:function:: remove_prefix(text: str, prefix: str) -> str

