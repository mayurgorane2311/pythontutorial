user_list = []
while(True):
    user = input("enter your detail and your information -")
    print("for quit enter q ")
    if user  == "q":
        break

    user_list.append(user)

    print(user_list)
print(user_list)
def list_fun():
    new_list = [i for i in user_list]
    print(new_list)
    return

def dict():
    new_dict = {i : f"your name is {i}" for i in user_list}
    print(new_dict)
    return

user_choice = input("which operation you want to perform here i.e 1.list  2.dic -")
if user_choice == 1:
    list_fun()
elif user_choice == 2:
    dict()


