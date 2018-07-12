from collections import OrderedDict

d = OrderedDict([('Company-id', 1),('Company-Name', 3)])
f = dict([('Company-id', 1),('Company-Name', 3)])

e = d.items()
print(e)
print(f)

names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]
professions_dict = {}
for i in range(len(names)):
    professions_dict[names[i]] = professions[i]

print(professions_dict)