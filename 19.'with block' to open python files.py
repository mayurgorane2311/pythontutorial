# importance of 'with' fuction is that it is not need close or open file
with open("15.mayur.txt") as f:
    a = f.readline()
    print(a)





f = open("15.mayur.txt", "rt")
print(f.readline())
# print(f.readline())
f.close()