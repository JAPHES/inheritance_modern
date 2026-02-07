#inheritance = it allows class to inherit attributes and methods from another class
#              helps with code reusability and extensibility
#              class child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("scobby")
cat = Cat("jack")
mouse = Mouse("brown")


print(dog.name)
print(dog.is_alive)
dog.eat()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()


