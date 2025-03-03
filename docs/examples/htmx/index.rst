.. _htmx:

############
HTMX + PyDOM
############

A recipe to integrate `HTMX <https://htmx.org>`_ with PyDOM.

Minimal Requirements
####################

To use HTMX with PyDOM, there are few requirements:

- Load HTMX library in your HTML page.
- Add transformers for HTMX attributes.
- (Optional) Add HTMX extensions:

  - Load the extension script in the head of the page.
  - Add transformers for the extension attributes (if needed).

Quick Start
###########

Under `utils/htmx_runtime.py <https://github.com/xpodev/pydom/blob/main/examples/htmx/utils/htmx_runtime.py>`_ you can find
utilities for simple integration with HTMX.

The recommended way to use it is just to copy the file to your project
and modify it to fit your needs (e.g. add more extensions).

Usage example:

.. code:: python

   import pydom as d
   from pydom.page import Page
   from pydom.context.context import get_context

   from utils import htmx_runtime as htmx

   # Optional: HTMX Extensions to be registered
   HTMX_EXTENSIONS: list[htmx.HTMXExtension] = [
       htmx.HTMXSSEExtension(),
       htmx.HTMXClassToolsExtension(),
   ]

   HTMX = htmx.HTMX()

   ctx = get_context()
   htmx.setup_htmx_transformers(ctx,
       # Optional: HTMX Extensions to be registered
       extensions=HTMX_EXTENSIONS)


   class BasePage(Page):
      def __init__(self, *args, **kwargs):
           super().__init__(
               *args,
               body_props=dict(
                   # Put the class-tools extension in the body
                   hx_ext=htmx.HTMXClassToolsExtension.name,
               ),
               **kwargs,
           )

       def head(self):
           yield HTMX.script()
           for ext in HTMX_EXTENSIONS:
               yield ext.script()


   # That's it! Now you can use HTMX attributes in your components
   def MyComponent():
       return d.Div(
           hx_get="/api/data",
           hx_trigger="click",
           hx_swap="outerHTML",
       )("Click me!")

Manual Integration
##################

.. code:: python

   from pydom.context.context import PropertyTransformer, get_context

   class MyPage(pydom.page.Page):
       def head(self):
           yield pydom.Script(
               src="https://unpkg.com/htmx.org@2.0.2",
               integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ",
               cross_origin="anonymous",
           )

   class HTMXTransformer(PropertyTransformer):
       def match(self, key: str, value):
           return key.startswith("hx_")

       def transform(self, key: str, value):
           # The full implementation is too long for this example.
           # You can find the full implementation in the utils/htmx_runtime.py file.
           raise NotImplementedError()

   ctx = get_context()
   ctx.add_prop_transformer(
       HTMXTransformer(),
       before=[HTMLEventsTransformer],
   )

Add Typing Support
##################

To add typing support and autocomplete for HTMX attributes, download
`this script <https://github.com/xpodev/pydom/blob/main/examples/htmx/utils/htmx_typing.py>`_, then you can run the following
command:

.. code:: bash

   python utils/htmx_typing.py typings

It will generate the necessary typing files for HTMX attributes,
enhancing your development experience with better autocompletion and
type checking.

Modify the generated file to fit your project needs, e.g. add htmx extensions.

Usage Notes
###########

You can differentiate between HTMX requests and regular requests by
checking the ``HX-Request`` header:

.. code:: python

   from pydom import d
   from pydom.page import Page

   class MyPage(Page):
       ...

   @router.get("/")
   @inject
   async def root(request: Request):
       is_htmx = request.headers.get("HX-Request") == "true"
       if not is_htmx:
           # Regular request, return the full page
           wrapper = MyPage()
       else:
           # HTMX request, return only the content
           wrapper = d.Fragment()

       inner = d.Div("Hello, world!")
       
       return render(wrapper(inner))

*Thanks to* `@elazarcoh <https://github.com/elazarcoh>`_ *for the guide and
the utilities.*