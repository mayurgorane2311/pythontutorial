# Exersise 2- faulty calculator
# Design a culculator which take operator and the two numbers as input from user
# 45 * 3 = 555 , 56+9 = 77, 56/6 = 4

import argparse
import sys


o = {"a":"+","s":"-","m":"*","d":"/"}
print("which of these operation you want to perform")
print(o.keys())

A = input("Enter the operator :")
if A == "a":
    B = int(input("Enter first num:"))
    c = int(input("Enter second num:"))
    if B == 56:
        if c== 9:
            print("ans = 77")
        else:
            print("ans:")
            print((B+c))
    elif B == 9:
        if c == 56:
          print("ans = 77")
        else:
           print("ans:")
           print((B + c))
    else:
        print("ans")
        print((B + c))

elif A == "s":
    B = int(input("Enter first num:"))
    c = int(input("Enter second num:"))
    print("ans")
    print(B-c)

elif A == "m":
    B = int(input("Enter first num:"))
    c = int(input("Enter second num:"))
    if B == 45:
        if c == 3:
            print("ans : 555")
        else:
            print("ans")
            print(B * c)
elif A == "d" \
          "":
    B = int(input("Enter first num:"))
    c = int(input("Enter second num:"))
    if B == 56:
        if c == 6:
            print("ans is 4")
        else:
            print("ans")
            print(B/c)
    else:
        print("ans")
        print(B/c)
