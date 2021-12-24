class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    @classmethod
    def from_dash(cls,string):             #this function for rohit
        return cls(*string.split(("-")))    # see here used '* argues fucntion



##object
mayur = student("Mayur",24,"B")
harry = student("Harry",29,"h")
rohit = student.from_dash("Rohit-54-t")# when such type of data than you required same type then create classmathod see above

print(rohit.age)