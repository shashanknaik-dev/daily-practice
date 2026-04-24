# with parameter no return value
class Calci:
    def __init__(self):
        self.brand="casio"
    def add(self,a,b):
        print(a+b)
c=Calci()
c.add(10,20)

# with parameter with return value
class Calci2:
    def __init__(self):
        self.brand="casio"
    def add(self,a,b):
        return a+b
c2=Calci2()
print(c2.add(10,20))
print(c2.brand)