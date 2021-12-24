try:
    f = open("does.txt")

except Exception as m:
    print(m)


else:
    print("this run when except is not run")

print("mayur")