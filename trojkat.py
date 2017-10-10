from math import sqrt


def triangle(a,b,c):
    p = (a + b + c)/2
    if 2 * p == a + b + c:
        s = sqrt(p * (p-a) * (p-b) * (p-c))
        print(s)
    else:
        print("error")

triangle(4,4,2)
