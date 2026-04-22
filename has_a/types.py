# types of has a relationship
# 1)composition
# 2)aggregation

# 1)composition 
class Os:
    def __init__(self):
        self.status="Active"
        print("os is installing")
    def getos(self):
        print("os is still installing")
class laptop:
    def __init__(self):
        self.Lname="lenovo"
        self.O=Os()
l1=laptop()
print(l1.Lname)
print(l1.O.status)
l1.O.getos()


class Os1:
    def __init__(self):
        self.status="active"
        print("os is active")
    def getos(self):
        print("os is still active")
class Computer:
    def __init__(self):
        self.brand="HP"
        self.O1=Os1()
c1=Computer()
print(c1.brand)
print(c1.O1.status)
c1.O1.getos()

class Radio:
    def __init__(self):
        pass
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class truck:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.R=Radio()
t1=truck(0,200)
print(t1.min)
print(t1.max)
t1.R.turnon(1)
t1.R.turnon(0)
del t1
# print(t1.min) #throws error because t1 is deleted 

# 2)aggregation
class Charger:
    def __init__(self):
        self.cname="iqoo charger"
        print("charger is ready")
    def getcharger(self):
        print("i love my charger")
class Phone:
    def __init__(self):
        self.pname="iqoo phone"
        self.c=""
        print("phone is ready")
    def hasphone(self,p):
         self.p=p
p1=Phone()
c1=Charger()
p1.hasphone(c1)
p1.p.getcharger()
del p1
print(c1.cname)


        