class Animal:
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.sound = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound
