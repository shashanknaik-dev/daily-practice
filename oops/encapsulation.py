class Book:
    def __init__(self,pages):
        self.__pages=pages
    def getter(self):
        return self.__pages
    def setter(self,values):
        self.__pages=values
b=Book(2000)
print(b.getter())
b.setter(3000)
print(b.getter())

# normal encapsulation
class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
p=Person()
p.setter("shashank")
# res=p.getter()
# print(res)
# or
print(p.getter())


# property function
class Person2:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
    getset=property(getter,setter)
p2=Person2()
p2.getset="shashu"
print(p2.getset)

# property decorator
class Person3:
    def __init__(self):
        self.__name=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,name):
        self.__name=name
p3=Person3()
p3.dataAccess="shashi"
res=p3.dataAccess
print(res)