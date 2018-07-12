import time

list_of_integers = [1, 12, 14, 282, 13, 1, 22, 89, 723, 14]

def even_index_in(x):
    t = time.process_time()
    z = [y for y in list_of_integers[::2] if y % 2 == 0]
    elapsed_time = time.process_time() - t
    print(elapsed_time)
    return z

even_index_in((list_of_integers))