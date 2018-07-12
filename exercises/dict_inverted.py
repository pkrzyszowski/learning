import pickle
my_map = {
    1: [1, 2, 3],
    2: 'b',
    3: 'c'
}

inv_map = {v: k for k, v in my_map.items()}

# print(inv_map)

with open('entry.pickle', 'wb') as f:
    pickle.dump(inv_map, f)