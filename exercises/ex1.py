a = list(range(1,1000))
print(a)
for x in a:
    for y in a:
        for z in a:
            if (x + y + z == 1000) and (x**2 + y**2 == z**2):
                print(x, y, z)
                print('FINISH')