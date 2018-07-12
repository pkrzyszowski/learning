class ParityError(Exception):
    pass

def hail_even_numbers(a):
    if a % 2:
        raise ParityError('down with {}'.format(a))
    print('hail even {}'.format(a))

hail_even_numbers(4)
try:
    hail_even_numbers(3)
except ParityError:
    print('dssdsds')