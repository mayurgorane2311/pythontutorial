# If you have any problem see tuturialpoint.com
# #Arithmatic operator
# print("5+6 is",5+6)
# print("5-6 is",5-6)
# print("5*6 is",5*6)
# print("5/6 is",5/6)
# print("15//6 is",15//6)    # only integeer value show
# print("5**6 is",5**6)     # expontiional
# print("5^6 is",5^6)
# #Assignment  operator
# x = 5
# print(x)
# x -=7
# print(x)

# #comparioson oprator
# i = 5
# print(i != 5)

# # logical operator
# a = True
# b = False
# print(a or b)

# # identity operator
# print(5 is not 6)

#  #Membership operator
# list = [3, 5, 45, 1, 85, 63, 10]
# print(325 not in list)

# #bitwise operator
# 0 - 00
#  1 - 0o1
# 2 - 20
# 3 - 11
# print(0 & 2)
# print(0 | 3)

#Exercise 4 Astrologer stars ex1
print("How Many Row You Want To Print -")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:

    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()


# z1 = int(input())
# b1 = bool(z1)
# print(b1)
# m = int(input())
# for g in range(1,m+1):
#     for k in range(1,g+1):
#         print("@",end=" ")
#     print()


# #Exercise 4 Astrologer stars ex2
# b = bool(input())
#
# a = int(input())
# def star(a,b):
#     if b == True:
#         c = 1
#         while c<=a:
#             print(c* "*")
#             c = c+1
#     else:
#         while a> 0:
#             print(a* "*")
#             a= a-1
#
# star(a,b)

# #Exercise 4 Astrologer stars ex2
