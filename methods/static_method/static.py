# static and class method
class Car:
    def __init__(self):
        self.brand="mahindra"
    @staticmethod
    def drift():
        print("car is drifting")
    @classmethod
    def accelerate(cls):
        print("car is accelerating")
c=Car()
c.drift()
c.accelerate()
print(c.brand)