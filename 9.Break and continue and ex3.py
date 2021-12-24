w = 0
# ex1
while (True):
    if w+1<5:
        print(w+1)
        w = w+1
        continue

    print(w+1, end=" ")
    if w==49:
        break # stop the loop
    w = w+1

# ex2
# Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")


# # exersise 3 guess the number
# j = 17
# print ("GAME RULE - 1)you have only 5 chance to guess\n",
#                    "2)you enter your number in between 0- 25  range\n")
# c = 0
# while(c<=4):
#     print(c+1)
#     c = c+1
#     print((6 - c), "number of guess left\n")
#     m1 = int(input("Guess the Number - "))
#
#     if m1>17:
#         print("Your number is not match try lesser number\n")
#         if m1>25:
#             print("OHHH'' out of range , please enter below 25\n")
#     elif m1<17:
#         print("your number is not match try bigger number\n ")
#     elif m1 == 17:
#         print("you won the game your number match perfectly\n")
#
#         break

