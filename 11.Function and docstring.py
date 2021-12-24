# built in function
# a = 9
# b = 8
# c = sum((a, b))
# print(c)

##User define fuction
#def is the keyword for defining a function.
#Optional documentation string (docstring) to describe what the function does.
def function1(a,b):
    # print("hello you are in fuction1")
    q = (a+b)
    return q

# m = function1(5, 7)
# print(m)

def fuction2(a, b):
    average = (a+b)/2
    # print(average)
    return average

# Main entry
a1 = int(input())
a2 = int(input())
v = fuction2(a1, a2)
# """this function whitch will calculate only two numbers""" # this is docstring
print( "aver" ,v)
v = function1(a1,a2)
print("sum of above",v)
print(fuction2.__doc__)




#def function2