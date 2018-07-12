mydict= {
    'Piaseczno': 'Piotrek' ,
    'Milanówek': 'Asia',
    'Warszawa': 'Piotrek'
}

reversed_dict = {}
for value in mydict.values():
    if value not in reversed_dict.keys():
        reversed_dict[value] = []
        for key in mydict.keys():
            if mydict[key] == value:
                if key not in reversed_dict[value]: reversed_dict[value].append(key)

print(reversed_dict)