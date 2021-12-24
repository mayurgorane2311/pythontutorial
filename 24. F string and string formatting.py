# # string formatting using % operator
# #Ex1 here %s is equal to number of variable
# name = "mayur"
# na = 5
# ma = 6
# same = " my name is %s %s %s " %(name,na,ma)
# print(same)

#Ex2  it call a.formating
import math

name = "mayur"
na =5
ma =6
#same = "your name is {1} {0} {2}"    #we can  change the sequence by using number see this
#a = same.format(name, na,ma)
#print(a)

#Ex3
a = f"this is {name} {na} {ma} {5*4} {math.cos(90)}"
print(a)