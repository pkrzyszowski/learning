hundred = list(range(101))
a = []
total = 0

for x in range(100):
    b = hundred[:]
    a.append(b)
    total += x
    b.append(total)

print(a)