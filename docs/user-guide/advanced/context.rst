.. _context:

#######
Context
#######

Context is an object that holds all the configuration for the rendering pipeline.
It contains :ref:`property-transformers`, :ref:`post-render-transformers` and the :attr:`injector <pydom.context.Context.injector>` object.

Each render process uses a context, which can be set by passing a context object to the ``render`` function as a keyword argument.
If a context is not provided, the :ref:`default context <default-context>` is used.

.. code:: python

    from pydom import render, Context

    context = Context()
    render(MyComponent(), context=context)

.. note::
  The above example creates a new context object, which means it's empty and doesn't have any transformers registered with it.

Transformers
############

Transformers are objects that can modify the rendering process.

There are two types of transformers:

- :ref:`Property Transformers <property-transformers>`
- :ref:`Post Render Transformers <post-render-transformers>`

To add a transformer to the context, use the :meth:`add_prop_transformer <pydom.context.Context.add_prop_transformer>` and :meth:`add_post_render_transformer <pydom.context.Context.add_post_render_transformer>` methods.

Transformers are applied in the order they are added to the context. It is possible to control the position of
the transformer by using the ``before`` and ``after`` arguments of the ``add_prop_transformer`` and ``add_post_render_transformer`` methods.

More information about transformers can be found in the :ref:`transformers section <transformers>`.

Dependencies
############

Dependencies are objects that can be injected into functions without explicitly passing them as arguments.
They are passed as keyword arguments to the function and are resolved by the context.

By default, all transformer methods can have dependency injection.

The default dependencies are:

- :class:`Context <pydom.context.Context>`
- :class:`RenderState <pydom.rendering.render_state.RenderState>` - Only available in the rendering process.

Injecting Dependencies
======================

To inject a dependency, add type annotations to the function arguments.

An example of injecting the ``RenderState`` dependency can be found on the :ref:`property transformer example <property-transformer-example>`.

Creating a Custom Dependency
============================

To create a custom dependency, use the :meth:`add <pydom.utils.injector.Injector.add>` method of the ``injector``.
Each injectable dependency must have a type associated with it, which is used to resolve the dependency when it is injected.

The injectable value can be anything, if it is callable, the return value of the call will be used as the value, this
allows for lazy initialization of the dependency.

.. note::
  Callable dependencies are called without any arguments.

Here is an example of a custom dependency:

.. code-block:: python
    :caption: Creating a custom dependency

    from pydom import get_context

    class User:
      ...

    def get_user():
        return {"name": "John"}

    get_context().injector.add(User, get_user)

Now the custom dependency can be injected into rendering functions using the ``User`` type.

Injecting Dependencies to an Outside Function
=============================================

The dependency injection system can also be used to inject dependencies into functions that are not part of the rendering process.

To achieve this, decorate the function with the ``inject`` method of the ``Context`` object.

.. code-block:: python
    :caption: Injecting dependencies to a function

    from pydom import get_context

    context = get_context()

    @context.inject
    def my_function(user: User):
        print(user)


The ``my_function`` function can now be called without any arguments and the ``User`` dependency will be injected.

Scoped Dependencies
===================

Scoped dependencies are dependencies that are only available during a specific scope, for example, during the rendering process.

To create a scoped dependency, use the ``scope`` method of the ``injector``
and pass a dictionary with the dependencies factory functions.

.. important::
  Since the dependencies are inspected only once when using the ``inject`` decorator, scoped dependencies must be forward declared.

  PyDOM provides a helper function to create scoped dependencies, the :func:`future_dependency <pydom.utils.injector.future_dependency>` function.
  This function takes a message to be raised when the dependency is accessed outside its scope.

To illustrate this, this is how PyDOM creates the ``RenderState`` dependency:

.. code-block:: python
    :caption: Creating a scoped dependency

    # Register the RenderState dependency as a future dependency
    context.injector.add(RenderState, future_dependency("RenderState is only available during the rendering process"))

    def render(...):
      render_state = RenderState(root=element, render_target="html", **render_state_data)
      with context.injector.scope({RenderState: lambda: render_state}):
          # RenderState is only available during this scope

.. _default-context:

Default Context
###############

By default, the context is created using the :meth:`Context.standard <pydom.context.Context.standard>` method.

The default context has the following transformers registered (in this order):

- :class:`FalsyTransformer <pydom.context.standard.transformers.FalsyTransformer>` - 
  Removes the following values from the element attributes: ``None``, ``False``.
- :class:`ClassTransformer <pydom.context.standard.transformers.ClassTransformer>` - 
  Converts the ``classes`` property to a space-separated string and changes the ``classes`` key to ``class``.
- :class:`SimpleTransformer <pydom.context.standard.transformers.SimpleTransformer>` - 
  Converts each of the following properties key to its corresponding HTML attribute:

  - ``html_for`` -> ``for``
  - ``access_key`` -> ``accesskey``
  - ``content_editable`` -> ``contenteditable``
  - ``cross_origin`` -> ``crossorigin``
  - ``tab_index`` -> ``tabindex``
  - ``use_map`` -> ``usemap``
  - ``col_span`` -> ``colspan``
  - ``row_span`` -> ``rowspan``
  - ``char_set`` -> ``charset``

- :class:`StyleTransformer <pydom.context.standard.transformers.StyleTransformer>` - 
  Converts any :class:`StyleSheet <pydom.styling.StyleSheet>` object to a css string.
- :class:`InnerHTMLTransformer <pydom.context.standard.transformers.InnerHTMLTransformer>` - 
  Sets the innerHTML property of an element with the ``dangerously_set_inner_html`` key.
- :class:`HTMLEventsTransformer <pydom.context.standard.transformers.HTMLEventsTransformer>` - 
  Converts the ``on_`` prefixed properties to their corresponding HTML event attributes.
- :class:`DashTransformer <pydom.context.standard.transformers.DashTransformer>` - 
  Converts each underscore in the property key to a dash.


Custom Context
##############

To create a custom context, simply create a new instance of the :class:`Context <pydom.context.Context>` class.

You can pass the created context to the ``render`` method to use it. If you want to use the custom context as the default context,
pass the created context to the :func:`set_default_context <pydom.context.context.set_default_context>` function.