# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
# print(fib(10))

def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)
print(fibR(10))