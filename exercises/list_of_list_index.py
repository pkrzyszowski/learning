list_of_integers = [2, 13, 14, 28, 29, 32, 44, 45, 98, 99]

x = [y for y in list_of_integers[::2] if y % 2 == 0]

print(x)
