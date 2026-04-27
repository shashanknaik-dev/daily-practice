class Parent:
    def __init__(self):
        self.a=10
class child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=20
c=child()
print(c.b)
print(c.a)

# connect parent class with child class using super() function

class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30
c=C()
print(c.a)
print(c.b)
print(c.c)

