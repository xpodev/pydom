.. _page:

####
Page
####

The page component is a the top-level component that represents a web page.
It is a container that holds all the other components that will be rendered on the page.

The default page component includes the elements for the following HTML structure:

.. code-block:: html
  :caption: Default page structure

  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>
        <!-- The page title property -->
      </title>
    </head>
    <body dir="ltr">
      <!-- Page children go here -->
    </body>
  </html>

Usage
#####

The page component can be used to create a new page by passing the following properties:

- ``title``: The page's title - if not provided, the tag will not be rendered
- ``html_props``: The props to insert inside the ``html`` tag
- ``head_props``: The props to insert inside the ``head`` tag
- ``body_props``: The props to insert inside the ``body`` tag

.. code-block:: python
    :caption: Creating a new page

    from pydom import Div, P
    from pydom.page import Page


    def my_awesome_page():
        return Page(title="My awesome page")(
            Div(classes="mx-auto mt-5")(
              Div(classes="text-center")(
                Div(classes="text-4xl font-bold")(
                  "Awesome page"
                ),
                P(classes="text-lg")(
                  "Welcome to PyDOM"
                )
              )
            )
          )
        

Custom Pages
############

You can create custom pages by extending the page component and overriding the default ``head`` and ``body`` methods.

.. code-block:: python
    :caption: Creating a custom page component

    from pydom import Div, Script
    from pydom.page import Page


    class MyPage(Page):
        def head(self):
            return (
                *super().head(), # Include the default head components
                Script(
                  src="https://cdn.tailwindcss.com"
                )
            )

        def body(self):
            return (
              Div(id="root")( # Wrap all the page children in a div with id root
                *self.children
              )
            )


    def my_awesome_page():
        return MyPage(title="My awesome page")(
            Div(classes="mx-auto mt-5")(
              Div(classes="text-center")(
                Div(classes="text-4xl font-bold")(
                  "Awesome page"
                ),
                P(classes="text-lg")(
                  "Welcome to PyDOM"
                )
              )
            )
        )

.. note:: 
  Both ``head`` and ``body`` methods should return an iterable of components, elements or primitives that will
  be rendered inside the ``<head>`` and ``<body>`` tags respectively.

API Reference
#############

+------------+--------+---------------------------------------------+----------------------+
| Name       | Type   | Description                                 | Default value        |
+============+========+=============================================+======================+
| title      | string | The page's title                            | ``None``             |
+------------+--------+---------------------------------------------+----------------------+
| html_props | dict   | The props to insert inside the ``html`` tag | ``{ "lang": "en" }`` |
+------------+--------+---------------------------------------------+----------------------+
| head_props | dict   | The props to insert inside the ``head`` tag | ``{}``               |
+------------+--------+---------------------------------------------+----------------------+
| body_props | dict   | The props to insert inside the ``body`` tag | ``{ "dir": "ltr" }`` |
+------------+--------+---------------------------------------------+----------------------+
