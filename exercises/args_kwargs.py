# Zmienna *args sygnalizuje, że do funkcji przesyłamy listę wartości, zaś zmienna **kwargs, że jest to słownik klucz-wartość.
def my_function(*args, **kwargs):
    for arg in args:
        print(str(arg))
    for key, value in kwargs.items():
        print(str(key) + " : " + str(value))

# Zauważmy, że traktujemy args jako zwykłą listę, zaś kwargs jako zwykły słownik. Więc po co te gwiazdki? Otóż dzięki
# nim możemy wywołać naszą funkcję następująco:
my_function(100, 200, 300, test=10, foo="oof")

# Przy czym ważne jest, aby pamiętać o kolejności, tzn. najpierw idą zmienne nienazwane, a potem nazwane.
