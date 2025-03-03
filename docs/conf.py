# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, datetime

sys.path.insert(0, "../src")

from pydom.version import version as __version__

project = "PyDOM"
author = "Xpo Development"
copyright = f"{datetime.date.today().year}, {author}"
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydata_sphinx_theme",
    "autoapi.extension",
    "sphinx_substitution_extensions",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates", "Thumbs.db", ".DS_Store"]

# -- Options for Auto Api ----------------------------------------------------
autoapi_dirs = ["../src/pydom"]
autoapi_ignore = []
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_root = "api-reference"
autoapi_keep_files = True
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True
autoapi_python_use_implicit_namespaces = True


def skip_submodules(app, what, name, obj, skip, options):
    if (
        name.startswith("pydom.html")
        or name.startswith("pydom.svg")
        or name.startswith("pydom.types.html")
    ):
        skip = True
    return skip


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "pydata_sphinx_theme"

html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_title = "PyDOM Documentation"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/xpodev/pydom",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/pytdom",
            "icon": "fa-brands fa-python",
        },
    ],
    "logo": {
        "image_light": "_static/images/logo-light.svg",
        "image_dark": "_static/images/logo-dark.svg",
    },
}

html_css_files = [
    "css/custom.css",
]

rst_prolog = f"""
.. |version| replace:: {version}
.. |br| raw:: html

   <br />
"""


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_submodules)
