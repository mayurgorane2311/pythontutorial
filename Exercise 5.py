#
# def gettime():
#     """This function will help you to get date and time"""
#     import datetime
#     return datetime.datetime.now()
# print("1 for Rohit")
# print("2 for Rohan")
# print("3 for Roni")
# try:
#     person = int(input())
# except:
#     print("Please enter only integer values i.e. \"1\", \"2\", or \"3\".")
#
# print("Now tell us what you want to do with Date")
# print("1 for Adding new Data")
# print("2 viewing old Data")
# try:
#     # dh reffers to Data Handeling
#     dh = int(input())
# except:
#     print("Please enter only integer values i.e. \"1\", or \"2\".")
#
# print("Now tell us what you want Exercise/Food")
# print("1 for Exercise")
# print("2 for Food")
# try:
#     # tod reffers to Type of data
#     tod = int(input())
# except:
#     print("Please enter only integer values i.e. \"1\", or \"2\".")
#
#
# if (person == 1):
#     # If person is Rohit
#     if (dh == 1):
#         if (tod == 1):
#             with open("a.rohit.exercise.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#         elif (tod == 2):
#             with open("tutorial 32.rohit.food.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#     elif (dh == 2):
#         if (tod == 1):
#             with open("a.rohit.exercise.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#         elif (tod == 2):
#             with open("tutorial 32.rohit.food.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#
# elif (person == 2):
#     # If person is Rohan
#     if (dh == 1):
#         if (tod == 1):
#             with open("tutorial 32.rohan.exercise.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#         elif (tod == 2):
#             with open("tutorial 32.rohan.food.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#     elif (dh == 2):
#         if (tod == 1):
#             with open("tutorial 32.rohan.exercise.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#         elif (tod == 2):
#             with open("tutorial 32.rohan.food.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#
# elif (person == 3):
#     # If person is Roni
#     if (dh == 1):
#         if (tod == 1):
#             with open("tutorial 32.roni.exercise.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#         elif (tod == 2):
#             with open("tutorial 32.roni.food.txt", "a") as file1:
#                 gettime()
#                 lock = str(input("Enter your Data:\n"))
#                 file1.write("["+str(gettime())+"]: "+lock+"\n")
#                 print("Successfully Recorded")
#     elif (dh == 2):
#         if (tod == 1):
#             with open("tutorial 32.roni.exercise.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#         elif (tod == 2):
#             with open("tutorial 32.roni.food.txt", "r") as file1:
#                 print(file1.read())
#                 print("Thanks for using our program.\n\n")
#
# else:
#     print("Please re-enter your values")