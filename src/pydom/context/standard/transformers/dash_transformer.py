from ....utils.functions import is_primitive

def dash_transformer():
    def matcher(key: str, value):
        return "_" in key and is_primitive(value)
    
    def transformer(key: str, value, element):
        dash_key = key.replace("_", "-")
        element.props[dash_key] = value
        del element.props[key]

    return matcher, transformer