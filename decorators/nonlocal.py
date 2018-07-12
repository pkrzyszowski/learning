def method():

    def method2():
        # In nested method, reference nonlocal variable.
        nonlocal value
        value = 100

    # Set local.
    value = 10
    method2()

    # Local variable reflects nonlocal change.
    print(value)

# Call method.
method()

# Nonlocal. Nonlocal is similar in meaning to global. But it takes effect primarily in nested methods.
# It means "not a global or local variable." So it changes the identifier to refer to an enclosing method's variable.