.. _fastapi:

###############
FastAPI + PyDOM
###############

The following is a guide on how to use PyDOM with `FastAPI <https://fastapi.tiangolo.com/>`_.

Basic Application
#################

Here is a basic FastAPI application that uses PyDOM to render a simple HTML page.

.. code-block:: python

    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    from pydom import Page, Div, render

    app = FastAPI()

    @app.get("/")
    async def read_root():
        return HTMLResponse(
            content=render(Page(Div("Hello, World!")))
        )
        
This application will render a simple HTML page with the text "Hello, World!".

For convenience, you can use the `Default response class <https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class>`_
to automatically return HTML responses.

Return Components Directly
##########################

As your application grows, you may want to return PyDOM components directly from your FastAPI routes instead of calling
the ``render`` function, which can be tedious.

Instead, you can register the ``render`` function as a custom encoder for the ``Component`` and ``Element`` classes.

This is done by setting the ``render`` function as the encoder for the ``Component`` and ``Element`` classes in the
``encoders_by_class_tuples`` dictionary.

.. code-block:: python

    from fastapi import encoders
    from pydom import Component, render
    from pydom.element import Element

    encoders.encoders_by_class_tuples[render] = (Element, Component)

This will allow you to return PyDOM components directly from your FastAPI routes without having to call the ``render`` function.

Like before, make sure the response class is set to ``HTMLResponse``.
