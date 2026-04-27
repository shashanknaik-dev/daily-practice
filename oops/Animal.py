class Animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Lion(Animal):
    pass
d=Dog()
c=Cat()
l=Lion()
d.eat()
d.sleep()
d.hunt()
c.eat()
c.sleep()
c.hunt()
l.eat()
l.sleep()
l.hunt()