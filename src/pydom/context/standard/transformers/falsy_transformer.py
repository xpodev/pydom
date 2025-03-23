from ....rendering.transformers import PropertyTransformer


class FalsyTransformer(PropertyTransformer):
    def match(self, _, prop_value) -> bool:
        return prop_value is False or prop_value is None

    def transform(self, prop_name, _, element):
        del element.props[prop_name]
