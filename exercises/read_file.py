
f = open('sample_file', 'r') # otwiera plik w trybie tekstowym do odczytu
print(f)
print(type(f))

b = f.read()
print(type(b))
print(len(b))
print('b: {}'.format(b))

c = f.read()
print(type(c))
print(len(c)) # 0 bo plik jest już 'przeczytany'
print('c: {}'.format(c))

f.seek(0) # ustawi nam wskaźnik pliku na początek

d = f.read()
print(type(d))
print(len(d))
print('d: {}'.format(d))

# read jest słaby do większych plików - wczytuje cały plik na raz do pamięci

# po skończonej pracy należy plik zamknąć
f.close()

# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newlines mode (deprecated)