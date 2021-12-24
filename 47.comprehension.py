'''
comprehension mean create new list or dic or set with also change sequence
'''
# # that is conventional method see follow
## for LIST
# list1 = []
# for i in range(20):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)
#
# # see this by comprehension
# ##ex1
# list1 = [i for i in range(20) if i % 2 == 0]   # here we used only one line for create list
# print(list1)

##ex2
# square = [i ** 3 for i in range(1,20)]
# print(square)

##for  dictionary
##Ex1
new_dict = {i : i **2 for i in range(20) if i % 2 ==0}
print(new_dict)

##Ex2
#see as conventional method
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

output_dict = {}

# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value

print("Output Dictionary using for loop:",
                              output_dict)