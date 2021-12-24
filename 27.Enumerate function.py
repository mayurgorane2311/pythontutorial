L = ["bhendi","aloo","flower","banana"]
# i = 0
# for item in L:
#     if (i%2) == 0:
#         print(f"buy {item}")
#         i += 1
#
#ex2 usinfd enumerate  function
# for i, item in enumerate(L):
#     if i%2 ==0:
#         print(f"buy {item}")

#EX 3
# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)