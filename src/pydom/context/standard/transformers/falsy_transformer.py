def falsy_transformer():
    def matcher(_, value):
        return not value

    def transformer(key: str, _, element):       
        del element.props[key]

    return matcher, transformer