# This feature in Python that allows the same operator to have different meaning according to the context is
# called operator overloading.
class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    def summery(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division}")

    @classmethod
    def change_passing(cls, newpassing):
        cls.passing = newpassing

    def __add__(self, other):
        return self.age + other.age

    def __truediv__(self, other):
        return self.age / other.age

    def __repr__(self):
        return print(f"name is ({self.name},{self.age} , {self.division})")

    def __str__(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division}")



##object
mayur = student("Mayur",24,"B")
lala = student("lala",50,"N")

#see if i want addition of age
# govind = mayur.age + lala.age   # see here we can addition  so we used dunder method
# print(govind)

# see now when we print only mayur variable then which one first show you see
print(mayur)        #see here by default print __str__ . when this function is not there the
