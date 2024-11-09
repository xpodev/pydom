from ....styling import StyleObject
from ...transformers import PropertyTransformer


class StyleTransformer(PropertyTransformer):
    def match(self, _, value):
        return isinstance(value, StyleObject)

    def transform(self, key: str, value: StyleObject, element):
        element.props[key] = value.to_css()
