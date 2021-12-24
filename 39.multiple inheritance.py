# In multiple inheritance, the features of all the base classes are inherited into the derived class.
# The syntax for multiple inheritance is similar to single inheritance.
#
# Example
class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    def summery(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division}")

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def summery2(self):
        return print(
            f"name is {self.name} and age is {self.age} and his division is {self.division} ")
#multiple inherentance see here two class are constitute in single class
class employes(student,Player):
    language = "C++"

    def printlanguage(self):
        print(self.language)

##object
mayur = student("Mayur",24,"B")
# #object variable

karan = employes("karan",30,"b")
print(karan.name)
print(karan.language)
karan.summery2() # here required only two attribute