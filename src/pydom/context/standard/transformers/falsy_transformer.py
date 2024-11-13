from ...transformers import PropertyTransformer


class FalsyTransformer(PropertyTransformer):
    def match(self, _, prop_value) -> bool:
        return not prop_value

    def transform(self, prop_name, _, element):
        del element.props[prop_name]
