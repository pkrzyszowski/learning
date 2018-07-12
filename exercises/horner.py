def horner(a):
    y = list(range(a,1,-1))
    for n in y:
        x = 2
        p = y[n]
        r = p * x + y[n]
        print(r)

horner(10)