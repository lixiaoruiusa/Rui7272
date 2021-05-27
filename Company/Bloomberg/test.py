class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("hello, " + self.name)


a1 = Animal("R")
a2 = Animal("L")

a1.say()
exit(666)



class Cat(Animal):
    def say(self):
        print("miao~~," + self.name)

class Dog(Animal):
    def say(self):
        print("wooo~~~," + self.name)


def say(animal: Animal):
    animal.say()


animal1 = Cat("Lebron")
animal2 = Dog("Green")


say(animal1)
say(animal2)


