# ##Ex1----------------------------------------------------------------@
# ##class
# #self mean which are object OR instant when we put in and called function required complete information
# class student:
#      passing = 36
#      def summery(self):
#         return print(f"name is {self.name} and age is {self.age} and his division is {self.division}j")
#
# ##object
# harry = student()
# mayur = student()
#
# ##object variable
# # here me add input so no need create new variable with new name try it
# harry.name = input("what is your name -")
# harry.age  = int(input("what is your age - "))
# harry.division = input("what is your division -")
#
# mayur.name = "Mayur"
# mayur.age  = 24
# mayur.division = "B"
#
# print(mayur.summery())

##Ex2------------------------------------------------------------------------@
# used __int__ funtion in class and object .I used above example
class student:
    passing = 36
    def __init__(self,aname,aage,adivision):
        self.name = aname
        self.age = aage
        self.division = adivision

    def summery(self):
        return print(f"name is {self.name} and age is {self.age} and his division is {self.division}")

##object
mayur = student("Mayur",24,"B")
# #object variable
# mayur.name = "Mayur"
# mayur.age  = 24
# mayur.division = "B"
# print(mayur.__dict__)         #possibility of print statement
# print(mayur.summery())
# print(mayur.division)