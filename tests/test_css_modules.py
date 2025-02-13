from pydom.styling import CSS

from .base import TestCase


class CSSModulesTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        styles = CSS.module("tests/css/styles.css")
        cls.card_class = styles.card
        cls.card_header_class = styles.cardHeader

    def test_class_name(self):
        styles = CSS.module("tests/css/styles.css")
        self.assertEqual(self.card_class, styles.card)
        self.assertEqual(self.card_header_class, styles.cardHeader)

    def test_relative_css(self):
        styles = CSS.module("./css/styles.css")
        self.assertEqual(styles.card, self.card_class)
        self.assertEqual(styles.cardHeader, self.card_header_class)
