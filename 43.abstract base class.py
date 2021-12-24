# An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# we can not create object of absractclass
from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type = "rectangle"
    sides = 4
    def  __init__(self):
        self.length = 4
        self.breath = 7

    def printarea(self):
        return self.length * self.breath

mayur = rectangle()
print(mayur.printarea())
