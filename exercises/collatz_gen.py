def collatz(n):
    x=[]
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3*n + 1
        yield int(n)
        x.append(n)
    print(x)

print(collatz(12))

# for x in collatz(10):
#     print(x)