#inheritance = it allows class to inherit attributes and methods from another class
#              helps with code reusability and extensibility
#              class child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def die(self):
        print(f"{self.name} as died.")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEEW!")

class Mouse(Animal):
    def speak(self):
        print("WOOF!")

dog = Dog("scobby")
cat = Cat("jack")
mouse = Mouse("brown")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.die()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.die()

print(cat.name)
print(cat.is_alive)
cat.eat()
dog.die()
