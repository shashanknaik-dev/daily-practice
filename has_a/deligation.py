class Radio:
    def turnon(self,x):
        if x==1:
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.R=Radio()
c1=Car(0,100)
print(c1.min)
print(c1.max)
c1.R.turnon(1)
c1.R.turnon(0)

# repeat
class Radio:
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class Car1:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.R=Radio()
c2=Car1(60,100)
print(c2.min)
print(c2.max)
c2.R.turnon(-1)
c2.R.turnon(1)