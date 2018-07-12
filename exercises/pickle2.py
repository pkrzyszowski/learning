import pickle
class Foo(object):
   y = 2
   def __init__(self, x, z):
     self.x = x
     self.z = z
   def bar(self, y):
     return self.x + y + self.z
   def baz(self, y):
     Foo.y = y
     print(Foo.y)
     return self.bar(y)


f = Foo(4, 2)
print(f.baz(Foo.y))
print(f.y)
print(pickle.dumps(f))