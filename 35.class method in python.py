class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    def summery(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division}")
        # if you don't want to 'self' then write this types
        # and also change class variable  like we here change 'passing' variable
        # instance method
    #first type of method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

   #second type of method
    @classmethod
    def change_passing(cls,newpassing):
        cls.passing = newpassing

##object
mayur = student("Mayur",24,"B")
harry = student("Harry",29,"h")

mayur.change_passing(40)
print(mayur.passing)             # see change passing,  here he change class attribute not instant attribute
print(mayur.sing("song"))       # here calling a first types of function or method