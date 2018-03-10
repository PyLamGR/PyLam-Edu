class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print("Felix has a color of:", felix.color)
print("While rover is colored:", rover.color)
print("And stumpy is kinda grumpy cause he only has", stumpy.legs, "legs")
