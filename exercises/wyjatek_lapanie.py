def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print('Nie dzieli sie przez zero')
        print('Wyjątek: {}, typ: {}'.format(e, type(e)))

divide(1, 1)
divide(8, 2)
divide(5, 0)

# Wyjątki służą do przerwania wykonywanego programu z jakiegoś wyjątkowego
# 	powodu, np:
# 		- dzielenie przez 0
# 		- błędu składni
# 	Wyjątki są klasami.
# 	Dziedziczą z BaseException.

# Można tworzyć własne wyjątki.
# 	Można łapać wyjątki "wbudowane" i własne.
# 	W normalnym użyciu nie powinno się łapać wyjątków poniżej `Exception`.
# 	Już samo łapanie `Exception` jest uważane za niepoprawne (łapie znacznie

# Jeśli wystąpi wyjątek (nie złapany) to na stderr pojawi się "Traceback".
# 	Jest to zrzut stosu. Innymi słowy prześledzona droga krok po kroku
# 	wykonania programu od miejsca najbliższego wyjątkowi do najbardziej
# 	zewnętrznego. Bardzo pomaga podczas debugowania programu.

# Wyrażenia `try ... except` moga byc zagnieżdżone jedno w drugim.