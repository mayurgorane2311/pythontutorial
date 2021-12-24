# simple class and object program
#see in which we protect our class variable by using underscore

class python:
    public = 5
    _protected = 6
    __private = 7

mayur = python()
print(mayur.public)            # see it run because it is public
print(mayur._protected)        # see this is also run because we run it in base class
#print(mayur.__private)        # here you show error because private attribute can't access so see below
print(mayur._python__private)  # see here so you required add underscore class name and then double underscore attribute