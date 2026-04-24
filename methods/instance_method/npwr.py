# no parameter with return value
class Calci:
    def __init__(self):
        self.numberofoperations=4
        self.color="red"
    def add(self):
        a=10
        b=20
        return a+b
c=Calci()
print(c.numberofoperations)
print(c.color)
print(c.add()) #or c=c.add()
               #   print(c)