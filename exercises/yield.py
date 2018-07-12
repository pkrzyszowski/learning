# Zwykłe funkcje po zawołaniu (call - użycie ()) dostaje 'prywatną' przestrzeń nazw,
# gdzie może przechowywać swoje wewnętrzne zmienne.
# Kiedy wykonanie funkcji dochodzi do return to zmienne lokalne są niszczone,
# a wartość zwracana przekazana do miejsca wywołania.
# Kolejne zawołanie tej funkcji tworzy NOWĄ 'prywatną' przestrzeń nazw i zmienne
# lokalne też są tworzone od nowa.

# Generatory różnią się od funkcji tym, że wyrażenie yield przekazuje jakąś wartość
# do miejsca wywołania, ale 'prywatna' przestrzeń nie jest niszczona.
# Kolejne wywołanie tej samej funkcji zacznie się tuż po yield w STAREJ przestrzeni,
# zmienne lokalne będą miały wartości takie jak tuż przed yield.
# Wyrażenie return zniszczy 'prywatną' przestrzeń.



def make_counter(x):
     print('entering make_counter')
     while x < 10:
         yield x
         print(x)
         x = x + 1

counter = make_counter(2)

# 1.Obecność słowa kluczowego yield w definicji make_counter
# oznacza, że nie jest to zwykła funkcja. To specjalny rodzaj
# funkcji, która generuje wartości przy każdym wywołaniu.
# Możecie myśleć o niej jak o funkcji kontynuującej swoje
# działanie: wywołanie jej zwraca obiekt generatora, który
# może zostać użyty do generowania kolejnych wartości x.
#
# 2.Aby uzyskać instancję generatora make_counter, wystarczy
# wywołać funkcję make_counter. Zauważcie, że nie spowoduje
# to jeszcze wykonania kodu tej funkcji. Można to stwierdzić
# na podstawie faktu, że pierwszą instrukcją w tej funkcji
# jest instrukcja print, a nic jeszcze nie zostało wypisane.
#
# 3.Funkcja make_counter zwraca obiekt będący generatorem.
# 4.Kiedy po raz pierwszy wywołamy next() na obiekcie generatora,
#  zostanie wykonany kod funkcji make_counter aż do pierwszej
# instrukcji yield, która spowoduje zwrócenie pewnej wartości.
#  W tym przypadku będzie to wartość 2, ponieważ utworzyliśmy
#  generator wywołując make_counter(2).
# 5.Kolejne wywołania next() na obiekcie generatora spowodują
# kontynuowanie wykonywania kodu funkcji od miejsca, w którym
#  wykonywanie funkcji zostało przerwane aż do kolejnego
# napotkania instrukcji yield. W tym przypadku następną linią
# kodu oczekującą na wykonanie jest instrukcja print, która
# wypisuje tekst "incrementing x", a kolejną - instrukcja
# przypisania x = x + 1, która zwiększa wartość x. Następnie
# wchodzimy w kolejny cykl pętli while, w którym wykonywana
# jest instrukcja yield, zwracająca bieżącą wartość x
# (obecnie jest to 3).
# 6.Kolejne wywołanie counter.next spowoduje wykonanie
# tych samych instrukcji, przy czym tym razem x osiągnie
# wartość 4. I tak dalej. Ponieważ make_counter zawiera
# nieskończoną pętlę, więc teoretycznie moglibyśmy robić
# to w nieskończoność: generator zwiększałby wartość x i
# wypluwał jego bieżącą wartość. Spójrzmy jednak na bardziej
# produktywne przypadki użycia generatorów.

def fibonacci(max):
    a, b = 0, 1       #(1)
    while a < max:
        yield a       #(2)
        a, b = b, a+b

with open('fib_sto.txt', 'w') as f:
    fib = fibonacci(100)
    for i in range(5):
        number = next(fib)
        f.write(str(number)) # nie dodaje końców linii
        f.write('\n')