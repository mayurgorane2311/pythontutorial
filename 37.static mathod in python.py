class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    @classmethod
    def from_dash(cls,string):             #this function for rohit
        return cls(*string.split(("-")))    # see here used '* argues fucntion
    ##see you already seen classmethod see above now we see staticmathod  see following example
    @staticmethod
    def new_mathod(stringvalue):
        a = print("this is a " + stringvalue )           #when we dont't want 'self' and 'cls' or empty then we used it

##object
mayur = student("Mayur",24,"B")
harry = student("Harry",29,"h")
rohit = student.from_dash("Rohit-54-t")# when such type of data than you required same type then create classmathod see above

rohit.new_mathod("man")   
#here some imp tip