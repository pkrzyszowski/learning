tablica = {"Wikipedia": "Wolna encyklopedia",
           (10, 12, 2006): "środa",
           255: 0xff}

# wypisanie wszystkich kluczy z tablicy
for klucz in tablica:
 	print(klucz)

# wypisanie wszystkich wartości z tablicy
for wartosc in tablica.itervalues():
 	print(wartosc)

# wypisanie jakie wartości są przypisane do jakich kluczy
for klucz, wartosc in tablica.iteritems():
 	print(klucz, '=>', wartosc)

# wyświetlenie wartości związanej z kluczem (łańcuchem) "Wikipedia"
if "Wikipedia" in tablica:
 	print(tablica["Wikipedia"])

print(tablica.get("Wikipedia", "brak klucza 'Wikipedia'"))