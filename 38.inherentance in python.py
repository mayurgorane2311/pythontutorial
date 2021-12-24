# Inheritance enables us to define a class that takes all the functionality from a parent class and allows us to add more
class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    def summery(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division} fee are due is {self.fee_due}")


class new_CLass(student):
    def __init__(self,aname,aage,adivision,fee):
        self.name = aname
        self.age = aage
        self.division = adivision        # see here overwriting is not objective but we can add new one in this function
        self.fee_due = fee


##object
mayur = student("Mayur",24,"B")
harry = student("Harry",29,"h")

arj = new_CLass("raj",45,"v",["twenty"]) # it is object for new class

arj.summery() # here we are only call it because we already print it at function

