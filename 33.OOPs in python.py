# class = template
# object = instant of class
# classis just "saccha"  you put in which make yoour parameter and ready of your object
##ex 1
# class
class student:
    passing = "above"
    pass

# instant variable mean object
mayur = student()
harry = student()

harry.name = "Harr"
harry.std  = 12

mayur.name =  "raja"
mayur.age  = 24

harry.passing
print(harry.passing)
mayur.passing = "ram"       # class me jo bhi hota hai wo ideal hota hai vasco class me se hi change karta ana chihiye
student.passing = "ramdas"
print(student.passing)
print(mayur.__dict__)       # create dict
mayur.passing = "ram"
print(mayur.passing)
print(harry.__dict__)
print(student.__dict__)