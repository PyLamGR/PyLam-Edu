class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


azor = Dog("Azor", "brown")
print(azor.name)
print(azor.color)
azor.bark()