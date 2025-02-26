# PyDOM

<p align="center">
  <img src="https://raw.githubusercontent.com/xpodev/pydom/refs/heads/main/docs/_static/images/logo.svg" alt="pydom-logo" width="200">
</p>

<p align="center">
  <strong>Simple to learn, easy to use, fully-featured UI library for Python</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/python-dom/">
    <img src="https://img.shields.io/pypi/v/pydom.svg" alt="PyPI version">
  </a>
</p>

PyDOM is a Python library that allows you to create web pages using a declarative syntax.

PyDOM provides a set of components that represent HTML elements and can be composed to create complex web pages.

## Quick Start

This is a quick start guide to get you up and running with PyDOM. The guide will show you how to setup PyDOM and integrate it with [FastAPI](https://fastapi.tiangolo.com/).

### Installation

First, install the PyDOM package.

```bash
pip install pydom
```

### Create Reusable Page

PyDOM provides a default page component that is the minimal structure for a web page.

The page can be customized by extending the default page component and overriding the `head` and the `body` methods.

More information about the default page component can be found [here](#page).

```python
# app_page.py

from pydom import Link, Page

class AppPage(Page):
    def head(self):
        return (
            *super().head(),
            Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
            )
        )
```

### Creating the FastAPI app

Lastly, create the `FastAPI` app and add an endpoint that will render the page when the user accesses the root route.

```python
# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydom import render, Div, P

form app_page import AppPage

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return render(
        AppPage(
            Div(classes="container mt-5")(
                Div(classes="text-center p-4 rounded")(
                    Div(classes="display-4")("Hello, World!"),
                    P(classes="lead")("Welcome to PyDOM"),
                )
            )
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
```

That's it! Now you can run the app and access it at [http://localhost:8000/](http://localhost:8000/).

It should display a page like this:

<p align="center">
  <img src="https://raw.githubusercontent.com/xpodev/pydom/refs/heads/main/docs/_static/images/quick-start.jpeg" alt="Quick Start">
</p>

## Documentation

The full documentation can be found at [our documentation site](https://pydom.dev/).
