import re

# re.match matches from the beginning of the string. In other words, it looks for an exact match between the string and the pattern
a = 'Joanna Krzyszowska z domu Michalska'

b = re.match('Krzyszowska', a)

print(b)

# re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string
c = re.search('dom', a)

print(c)

# findall() – finds all the occurrences of match and return them as a list
d = re.findall('lska', a)

print(d)

# finditer() – finds all the occurrences of match and return them as an iterator.
e = re.finditer('ska', a)

print(e)

