class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age

# Main routine
dog1 = Dog("luna", 4, "brown")
dog2 = Dog("bob", 3, "white")

print(Dog.details(dog1))
print(Dog.details(dog2))