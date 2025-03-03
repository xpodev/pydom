pydom.errors
============

.. py:module:: pydom.errors


Exceptions
----------

.. autoapisummary::

   pydom.errors.Error
   pydom.errors.RenderError
   pydom.errors.DependencyOutOfContextError


Module Contents
---------------

.. py:exception:: Error

   Bases: :py:obj:`Exception`


   Base class for all pydom exceptions.


.. py:exception:: RenderError

   Bases: :py:obj:`Error`


   Raised when an error occurs while rendering an element.


.. py:exception:: DependencyOutOfContextError

   Bases: :py:obj:`Error`


   Raised when a dependency is requested that is not in the context.


