# multileval inherentance
##In multiple inheritance, the features of all the base classes are inherited into the derived class.
class dad:
    song = "super"

class son(dad):
    total_song = 8
    def son_function(self):
        return f"I am passinate about me {self.total_song} song"

class grandson(son):
    total_song = 10
    def grand_son_function(self):
        return f"papa i am also passinate about {self.total_song}"

keshav = dad()
rajaram = son()
mayur = grandson()

print(mayur.total_song) # here he take grandson attribute
print(mayur.grand_son_function())  #see here he also take son attribute
print(mayur.song)