# # maxgun tech que on population
# population = {'china': 143, 'india': 136, 'USA': 32, 'pakistan': 21}
# print(population)
# def add():
#     country = input("enter your country name - ")
#     if country in population:
#         print("you are entered country is already in dictionary")
#         return
#     praja = float(input("enter country population - "))
#     population[country] = praja
#     return
#
# def delete():
#     country = input("enter country name which you want to delete from a dictionary---")
#     if country not in population:
#         print("you can't delete this country because this is not exist in your dictionary")
#         return
#     del population[country]
#     return
#
# def query():
#     country = input("enter country name for any queries releted -")
#     if country not in population:
#         print("this country is not in dictionary")
#         return
#     else:
#         print(f"{country} and is polulation is {population[country]}")
#
# def main():
#     user_input = input("what kind of chenges you have want in dictionary i.e add/delete/query -")
#     user_input.lower()
#     if user_input == "add":
#         add()
#         print(population)
#     elif user_input == "delete":
#         delete()
#         print(population)
#     elif user_input == "query":
#         query()
#     else:
#         print('wrong input by user')
#
# main()

# second question
π= 3.14
def circumference():
    area_circum = 2 * π * u
    print(f"circumtance of circle is - {area_circum}")
    return

def area():
    area_circle = π * u * u
    print(f"area of circle is - {area_circle} ")
    return

def diameter():
    dia_of_circle = 2 * u
    print(f"diameter of circle is {dia_of_circle}")
    return

print("1.circumference")
print("2.area")
print("3.diameter")
print("4.All")
print("5.quit")

while(True):
    user = int(input("enter your response-"))
    if user == 1:
        u = int(input("enter value -"))
        circumference()
    elif user == 2:
        u = int(input("enter value -"))
        area()
    elif user == 3:
        u = int(input("enter value -"))
        diameter()
    elif user == 4:
        u = int(input("enter value -"))
        circumference()
        area()
        diameter()
    elif user == 5:
        print("you out from process ")
        break
    else:
        print("wrong input please try again")



