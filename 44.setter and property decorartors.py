class student:
    def __init__(self,fname,surname):
        self.fname = fname
        self.surname = surname

    def personal_email(self):
        return f"this student name is {self.fname} {self.surname}"

    @property    # when we write this function we don't need to write function parathesis at time of call it see below
    def email(self):
        return f"{self.fname}.{self.surname}23@gmail.com"

    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.surname = name.split(".")[1]

#object
mayur = student("mayur","gorane")

print(mayur.email)   # see here we not used parathesis '()' despite this is a function that a used of praperty function
mayur.fname = "rajaram"   # see here we can chenge constructor variable
print(mayur.email)        # see here our chenges edited here


mayur.gmail = "this.that23@gmail.com"      # for this changes we used setter here we wand to change first and surname
print(mayur.gmail)                         # see above first of all set which function want to set


print(mayur.fname)
