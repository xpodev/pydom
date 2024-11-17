import unittest

from pydom import render
from .components import App, Page


class NestedComponentsTest(unittest.TestCase):
    def test_nested_components(self):
        self.assertEqual(
            render(App()),
            '<div class="card"><h3 class="card-title">Card title</h3><hr><div></div></div>',
        )

    def test_page_inheritance(self):
        self.maxDiff = None
        self.assertEqual(
            render(Page(App())),
            '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="/static/style.css"></head><body dir="ltr"><div class="card"><h3 class="card-title">Card title</h3><hr><div></div></div></body></html>',
        )
