# zip() function- it will take multiple lists say list1, list2, etc and transform them into a single list of tuples
# by taking the corresponding elements of the lists that are passed as parameters

list1 = ['A','B','C']
list2 = [10,20,30]
a = zip(list1, list2)
print(list(a))

x = 'foo'
y = x
print(x) # foo
y += 'bar'
print(y) # foo