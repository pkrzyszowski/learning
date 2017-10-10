list_of_strings = ["mama", "tata", "babcia", "dziadek"]
list_of_integers = [1, 3, 2, 5, 6, 13, 7]

list_of_strings.sort()
# sorted_list = sorted(list_of_strings)

# print(sorted_list)


# What is the difference between sorted(list) vs list.sort()?

# list.sort mutates the list in-place & returns None
# sorted creates a new list from the old & returns the new one, sorted.


# when to use which?

# Use list.sort when you do not wish to retain the original sort order
# (Thus you will be able to reuse the list in-place in memory.)
# and when you are the sole owner of the list
# (if the list is shared by other code and you mutate it,
# you could introduce bugs where that list is used.)

# Use sorted when you want to retain the original sort order or when you wish
# to create a new list that only your local code owns.