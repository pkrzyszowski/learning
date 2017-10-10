my_list = [{'name':'Homer', 'age':39}, {'name':'Milhouse', 'age':10}, {'name':'Bart', 'age':10} ]
newlist = sorted(my_list, key=lambda k: k['name'])

print(newlist)