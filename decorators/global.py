def method():
    # Change "value" to mean the global variable.
    # ... The assignment will be local without "global."
    global value
    value = 100

value = 0
method()

# The value has been changed to 100.
print(value)

# This program uses the global keyword. In method(), we use the statement "global value."
# This means that the identifier "value" refers to the global "value," which is accessed outside the method.