.. _flask:

#############
Flask + PyDOM
#############

Here is a quick guide on how to use PyDOM with Flask.

A Minimal Application
#####################

The most basic way to use PyDOM with Flask is to render a PyDOM component in a Flask view function.

.. code-block:: python

    from flask import Flask
    from pydom import P, render

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return render(P("Hello, world!"))

This corresponds to `A Minimal Application <https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application>`_ in the Flask documentation.

Making PyDOM Decorators
#######################

It might be a little cumbersome to use the ``render`` function in every view function.
To make it easier, you can create a decorator that automatically renders the PyDOM component.

.. code-block:: python
    :caption: PyDOM Decorator

    from functools import wraps

    from flask import Flask
    from pydom import P, render

    app = Flask(__name__)

    def pydom(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            return render(view(*args, **kwargs))
        return wrapper

    @app.route("/")
    @pydom
    def hello_world():
        return P("Hello, world!")

Now you can use the ``pydom`` decorator to render PyDOM components in your Flask view functions.