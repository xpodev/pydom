import unittest

from pydom import render, Div, Script, Style


class EscapingComponentsTest(unittest.TestCase):
    def test_escaping(self):
        self.assertEqual(
            render(
                Div(
                    "<script>console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }</script>"
                )
            ),
            "<div>&lt;script&gt;console.log(&#x27;hello world&#x27;); if (a &lt; 2) { console.log(&#x27;a is less than 2&#x27;); }&lt;/script&gt;</div>",
        )

    def test_escaping_style(self):
        self.assertEqual(
            render(Style("body { color: red; }")),
            "<style>body { color: red; }</style>",
        )

    def test_escaping_script(self):
        self.assertEqual(
            render(
                Script(
                    "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
                )
            ),
            "<script>console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }</script>",
        )
