class MyFirstClass():
    # pierwszy argument jest obowiązkowy, zwyczajowo nazywany self
    def hello(self):
        print("Hello!")
        print(self)
        print(type(self))
        print(id(self))


a = MyFirstClass()
a.hello()
# a tu wydarzyło się coś dziwnego, metoda hello przyjmuje jeden argument, nie podaliśmy go.
# A zadziałało, żaden wyjątek nie wyskoczył. Dlaczego?
# https://docs.python.org/3/tutorial/classes.html#method-objects
# pierwszy argument jest przekazywny automatycznie

b = MyFirstClass()
b.hello()
#
MyFirstClass.hello(a)
#
print('-' * 80)
#
print(type(a.hello))
print(type(MyFirstClass.hello))
# # pierwszy argument (self) jest konkretną instancją klasy