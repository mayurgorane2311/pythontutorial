
# see how to print sequence 1) find init 2) then find inherent class init 3) then find class variable of B and then A
# ones we copy class A Instant to B then he see that you overide so avoide this problem we used super() see below
class A:
    ram = "I am in class A"
    def __init__(self):
        self.one = "i am in instant A"
        self.two = " you are in instant A"
        self.three = "special"

# override class A
class B(A):
    ram = "I am in class B"
    def __init__(self):
        super().__init__()                       # ab run honga 'special'
        self.one = "i am in instant B"           # when we commitout and this line then he print class A instant
        self.two = " you are in instant B"

# object
a = A()
b = B()

print(b.three)   # see here print class B attribute ,because we override, see same name of variable
print(b.one)
