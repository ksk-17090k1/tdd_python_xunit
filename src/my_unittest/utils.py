def get_test_methods(cls: object):
    return [
        method_name
        for method_name in cls.__dict__
        if method_name.startswith("test") and callable(getattr(cls, method_name))
    ]
