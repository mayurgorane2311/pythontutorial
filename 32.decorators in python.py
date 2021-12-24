## Decorator in python
##Ex 1     we can change function name and then call it
# def raja():
#     print("mayur don")
# raja()
# saja = raja
# saja()

##Ex2  two function put in in another function
# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x - 1
#
# def operate(func, x):
#     result = func(x)
#     return result
# o = operate(inc,6)
# g = operate(dec,6)
# print(o)
# print(g)

##ex3
#function  is called annother function
def func1(ran):                    # see function
    def sampal():                  # anather function
        print("executed")
        ran()                      # here we called function variable see carefully not function
        print("start executed")
    return sampal

def applied_ona():
    print("implement")
applied_ona = func1(applied_ona)
applied_ona()




