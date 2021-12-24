# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator. join function is must be used for string
lis = ["raina","dhoni","jadeja","brovo","FAF"]
lis.append("kohali")
lis.insert(2,"rohit")

g = " & ".join(lis)
print(g)