def event(event: str, **attrs):
    def wrap(f: classmethod):
        f.__is_event__ = True
        f.__event__ = event
        return f
    return wrap