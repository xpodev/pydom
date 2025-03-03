.. _tailwindcss:

####################
Tailwind CSS + PyDOM
####################

The only requirement to make tailwindcss work with PyDOM is having
`Tailwind CLI <https://tailwindcss.com/docs/installation/tailwind-cli>`_ installed.

Quick Start
###########

First, install Tailwind CLI `See installation instructions <https://tailwindcss.com/docs/installation/tailwind-cli>`_.

Tailwind CSS v3
===============

1. Create a new Tailwind configuration file:

.. code:: bash

    npx tailwindcss init

2. Add the following to your Tailwind configuration file:

.. code:: js

    module.exports = {
      content: ["./src/**/*.{py}"],
    };

Tailwind CSS v4
===============

If you have Tailwind v4 installed, you can simply add the following to your CSS file:

.. code:: css

    @import "tailwindcss";
    @source "./src/**/*.{py}";


Generating CSS
==============

To generate the CSS file, run the following command:

.. code:: bash

    npx tailwindcss -i ./input/style.css -o ./output/style.css --watch

Add the generated CSS file to your PyDOM pages:

.. code:: python

    from pydom import Page, Link

    class MyPage(Page):
        def head(self):
            return (
                *super().head(),
                Link(
                  rel="stylesheet",
                  href="/output/style.css"
                )
            )

Now you can use Tailwind CSS classes in your PyDOM components:

.. code:: python

    from pydom import Div

    def MyComponent():
        return Div(
            "Hello, world!",
            classes="text-center text-2xl text-red-500"
        )

That's it! Now you can run your app and see the Tailwind CSS styles applied.

VSCode Tailwind CSS IntelliSense
################################

To enable Tailwind CSS IntelliSense in VSCode, you can install the `Tailwind CSS IntelliSense <https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss>`_ extension.

We need to configure the IntelliSense extension to work with PyDOM. Add the following to your VSCode settings:

.. code:: json

    {
      "tailwindCSS.includeLanguages": {
        "python": "html"
      },
      "tailwindCSS.classAttributes": [
        "classes",
      ]
    }

You can add more attributes to the ``tailwindCSS.classAttributes`` list if you use different
attribute names for classes in your PyDOM components.
