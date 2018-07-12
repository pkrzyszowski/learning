# Map applies a function to all the items in an input_list.

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared)

# filter creates a list of elements for which a function returns true.
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Reduce is a really useful function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list.
# For example, if you wanted to compute the product of a list of integers.
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)