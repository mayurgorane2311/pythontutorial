# # Ex1 scope
# def fuction1(n):
#     print(n, "I have print")
#
# fuction1("this is me")


# # Ex2 on global and local variable
# l = 10                 # Global variable
# def fuction1(n):
#     # l = 5            # Local variable
#     m = 8              # Local variable
#     global l           # see we can not change global value only can change by calling global in local
#     l = l +45
#     print(l,m)
#     print(n,"hello dear")
# fuction1("see")


# # Ex3 use of global variable
x = 89
def mayur():
    x = 3
    def murli():
        global x          # global variable is not work in local varible. Try this exam
        x = 10
    print("before",x)
    murli()
    print("after",x)
mayur()
print(x)

