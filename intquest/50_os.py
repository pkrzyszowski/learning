import os

a = os.path.exists('/etc/hosts')
b = os.path.isfile('/etc/hosts')
c = os.path.isdir('/etc/hosts')
d = os.path.getsize('/etc/hosts')
e = os.path.getmtime('/etc/hosts')
print(a)
print(b)
print(c)
print(d)
print(e)