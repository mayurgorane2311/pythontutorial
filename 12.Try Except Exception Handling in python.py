#First, try clause is executed i.e. the code between try and except clause.
#If there is no exception, then only try clause will run, except clause is finished.
#If any exception occured, try clause will be skipped and except clause will run.

print("enter num 1")
n1 = input()
print("enter num 2")
n2 = input()
try:
    print("Ans is ",
      int(n1)+int(n2))
except Exception as e:
    print(e)

print("mayur gorane")