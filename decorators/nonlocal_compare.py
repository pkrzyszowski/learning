# Nonlocal - In short, it lets you assign values to a variable in an outer (but non-global) scope

# x = 0
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# outer()
# print("global:", x)
# inner: 2
# outer: 1
# global: 0


# x = 0
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# outer()
# print("global:", x)
# inner: 2
# outer: 2
# global: 0

x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2