from .Animal import Animal


class Dog(Animal):
    def __init__(self):
        super().setSound("Bark")

    def digHole(self):
        print("Dug a Hole")
