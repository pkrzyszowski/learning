try:
    x = 10 + 'Python'
    raise Exception('NIe nienie')
except:
    print('incompatible operand types to perform sum')


# voting_age = 15
# if voting_age < 18:
#     raise ValueError('voting age should be atleast 18 and above')

a = -10
assert a > 0