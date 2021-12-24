'''
1)iterable - we see any object is iterable or not i.e list , string is iterable
2)Itrators - now any object is iterate one  by one i.e when we create for loop then any list is print in console is
3)iteration - the complete process of above is called iteration

'''


# for i in range(20):
#     print(i)
# but if we want to print big number is possible hence we used genrators see belows first of all we create function

def gen(n):
    for i in range(n):
        yield i
g = gen(4520)
print(g.__next__())     # see here we get one number
print(g.__next__())     # see here we get one number
print(g.__next__())     # see here we get one number
print(g.__next__())     # see here we get one number
print(g.__next__())     # see here we get one number
                        # when we print same thing then we get next numbers