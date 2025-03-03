pydom.utils.injector
====================

.. py:module:: pydom.utils.injector


Attributes
----------

.. autoapisummary::

   pydom.utils.injector.T
   pydom.utils.injector.InjectFactory


Classes
-------

.. autoapisummary::

   pydom.utils.injector.Injector


Functions
---------

.. autoapisummary::

   pydom.utils.injector.future_dependency


Module Contents
---------------

.. py:data:: T

.. py:data:: InjectFactory
   :type:  typing_extensions.TypeAlias

.. py:class:: Injector(defaults: Optional[Dict[type, Any]] = None)

   A simple dependency injection container

   To get an instance of a class, you can use the `injector` property of the `Context` class.


   .. py:attribute:: dependencies
      :type:  Dict[type, Callable]


   .. py:method:: add(cls: Type[T], factory: InjectFactory, /) -> None
                  add(cls: Type[T], instance: T, /) -> None


   .. py:method:: inject(callback: Callable) -> Callable


   .. py:method:: scope(dependencies: Dict[type, InjectFactory])


.. py:function:: future_dependency(message: str)

