# #Ex1
# import random
# c= 0
# while (c<=5):
#     print(c + 1)
#     c = c + 1
#     print((6 - c), "number of guess left\n")
#     user = int(input("enter number\n"))
#     if user >= 0 and user <=5:
#         randam_numbers = random.randint(0,5)
#         print(randam_numbers)
#     else:
#         print("wrong input")
#         break

# #Ex2
# import random
#
# rand = random.Random() *100
# print(rand)

# #EX3
import random

list = ["star","sony","aaj tak","indiatv"]
choice = random.choice(list)
print(choice)

