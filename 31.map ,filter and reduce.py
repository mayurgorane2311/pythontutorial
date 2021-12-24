###----------------------------- map() function
# Syntax : map(fun, iter)

##Ex1
# Python program to demonstrate working
# of map.
# Return double of n
# def multipliction(m):
#     return m*m
#
# value = [4,5,89,5,2,45,8,56,4,7,45]
# ma = map(multipliction,value)
# print (list(ma))             # you should write 'list' at time of print object but you can write above or below see

##Ex2
#We can also use lambda expressions with map to achieve above result.
# Double all numbers using map and lambda
# value = [4, 5, 89, 5, 2, 45, 8, 56, 4, 7, 45]
# ma = list(map(lambda m:m*m,value))
# print((ma))

##Ex3
# Add two lists using map and lambda
# value = [4, 5, 5, 2, 4, 7, 45] # here not print '45' so it required equal value
# unit =  [7, 8, 2, 3, 5, 4]
# ans = map(lambda x,y:x+y, value,unit)
# print(list(ans))

##Ex4
# List of strings
# l = ['sat', 'bat', 'cat', 'mat']
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# #Ex5
# #convert string to integer by using map function
# n1 = ["3","5","15"]
# n1 = list(map(int,n1))       # see variable name is same
# n1[2]= n1[2]+ 1
# print(n1)



####----------------------------- Filter()
##Ex1
# #run both function in one map
# # See this example somothing unique because here two fucntion but place in iteration place  see care fully
# ## here also used filter to list before map it
# def m1(m):
#     return m*m
#
# def m2(m):
#     return m*m*m
# function = [m1,m2]
# value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# def f1(num):
#     return 5<= num <=13
# filtred = filter(f1,value)
# print()
#
# for i in filtred:
#     nmuber_list = map(lambda x:x(i), function)
#     print(list(nmuber_list))

##Ex2
# # a list contains both even and odd numbers.
# seq = [0, 1, 2, 3, 5, 8, 13]
#
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
#
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

#_______________________Reduce()
#Python’s reduce() is a function that implements a mathematical technique called folding or reduction
##reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value. i
# ##Ex1
# from functools import reduce
#
# lis = [2,3,4,5,]
# single = reduce(lambda x,y:x*y,lis)
# print(single) # here not used 'list'




