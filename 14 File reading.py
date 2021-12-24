# Refer programiz.com if have any problem
f = open("15.mayur.txt", "rt")
# print(f.readline())
# print(f.readline())
# print(f.readline())

#content = f.read(55555)
#print(content)

for line in f:
    print(line, end=" ")

f.closed