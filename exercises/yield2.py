def f(n):
    for x in range(n):
        yield x**3

for x in f(5):
    print(x)