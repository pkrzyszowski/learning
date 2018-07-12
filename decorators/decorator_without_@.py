def decorator(decorated_func):
    print('Wewnątrz dekoratora')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    return decorated_func


def hello_function():
    print('hello')


hello_function()
print(hello_function)
print(id(hello_function))
print(80 * '-')
hello_function = decorator(hello_function)
print(80 * '-')
print(hello_function)
print(id(hello_function))
hello_function()
hello_function()