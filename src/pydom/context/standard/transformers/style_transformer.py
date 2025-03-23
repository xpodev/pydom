from ....styling import StyleSheet
from ....rendering.transformers import PropertyTransformer


class StyleTransformer(PropertyTransformer):
    def match(self, _, value):
        return isinstance(value, StyleSheet)

    def transform(self, key: str, value: StyleSheet, element):
        element.props[key] = value.to_css()
