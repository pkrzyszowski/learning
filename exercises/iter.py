obj = [1,2,3]
x = iter(obj)
for i in iter(obj):
    print(next(x))
    print(x.__next__())

for i in obj:
    print(i)

# Wbudowana funkcja iter() przyjmuje dowolny obiekt i próbuje
# zwrócić iterator zwracający kolejne elementy danego obiektu.
#
# Funkcja iter() rzuca wyjątek TypeError, jeśli dany
# obiekt nie obsługuje iteracji.
#
# Obiekt jest iterowalny jeśli dla niego funkcja iter() zwróci iterator.
#
# Część wbudowanych typów danych jest iterowalna: lista, tupla, słownik, zbiory.

# można wywołać next tak:
#     x.__next__()
# albo tak:
#     next(x)