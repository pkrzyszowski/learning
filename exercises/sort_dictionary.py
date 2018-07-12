def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

d = {'licznik': 3, 'bazadanych': 'master', 'serwer': 'mpilgrim', 42: 'douglas', 'uid': 'sa'}

sortedDictValues1(d)
