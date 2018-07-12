class UnexpectedTypeException(Exception):
    pass


def expected_type(etype):
    def wrapper(f):
        def wrapped(*args, **kwargs):
            result = f(*args, **kwargs)
            if not isinstance(result, etype):
                raise UnexpectedTypeException("Was expecting instance of: %s" % (etype))
            return result
        return wrapped
    return wrapper


if __name__ == '__main__':
    @expected_type(int)
    def return_something(something):
        return something


    return_something('Hello world')
