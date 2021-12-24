#
import random
choices = ['snake', 'water', 'gun']
game_counter = 0    # it will count number of strike to exit from the game
cpu = 0             # It will keep score of computer
player = 0          # It will keep score of player
print("\n", '\t'*5, "Welcome to Snake-Water-Gun game:\n")
while game_counter < 10:

    print((10-game_counter),"chance left")
    game_counter += 1
    cpu_choice = random.choice(choices)     # It will select value from choices list randomly
    user_choice = input("Enter your selection: snake/water/gun: ").lower()  # It takes value from user and convert into lower case
    if user_choice in choices:
        if cpu_choice == "snake" and user_choice == 'gun':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "snake" and user_choice == 'water':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == "gun" and user_choice == 'water':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "gun" and user_choice == 'snake':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == "water" and user_choice == 'snake':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tPlayer won this strike\n")
            player += 1
        elif cpu_choice == "water" and user_choice == 'gun':
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tComputer won this strike\n")
            cpu += 1
        elif cpu_choice == user_choice:
            print(f"Player: {user_choice}\tComputer: {cpu_choice}\tOops! Same guess, no one won this strike\n")
    else:
        print("invalid input, Try again\n")


if player == cpu:
    print(f"Match tied: Player: {player}\tComputer: {cpu}")
elif player > cpu:
    print(f"Finally Player won the game: Player: {player}\tComputer: {cpu}\tTie: {10-player-cpu}")
else:
    print(f"Finally Computer won the game: Computer: {cpu}\tPlayer: {player}\tTie: {10-player-cpu}")



# import random
#
# print("welcome to snake water gun game\n")
# print("This game is not real world based game , but a survival simulation game\n")
# print("WARNING - We give you ten chance to survival if your luck better")
# list = ['snake', 'water', 'gun']
# p = 0
# cpu = 0
# c=0
# while(c<= 10):
#     c= c+1
#     print("Your life chance ramain -",11-c)
#     u = (input("Enter randam charactor i.e snake  , water ,gun\n"))
#     com = random.choice(list)
#     if u in list:
#         if u == 'snake' and com == "gun":
#             print(f"p:{u}\tcpu:{com }\t you won this game")
#             p +=1
#         elif u == 'snake' and com == "water":
#             print(f"p:{u}\tcpu:{com}\t cpu won this game")
#             cpu +=1
#         elif u == 'gun' and com == "snake":
#             print(f"p:{u}\tcpu:{com}\tcpu won this game")
#             cpu +=1
#         elif u == 'snake' and com == "gun":
#             print(f"p:{u}\tcpu:{com}\tcpu won this game")
#             cpu +=1
#         elif u == 'snake' and com == "water":
#             print(f"p:{u}\tcpu:{com}\tcpu won this game")
#             p +=1
#         elif u == 'water' and com == "snake":
#             print(f"p:{u}\tcpu:{com}\tcpu won this game")
#             p +=1
#         elif u == com:
#             print(f"p:{u}\tcpu:{com}\tdraw")
#     else:
#         print("invalid input")
# if p == cpu:
#     print(f"match ties\t p:{p}\tcpu{cpu} ")
# elif p> cpu:
#     print(f"p won game\t p:{p}\tcpu{cpu}\ttie {10-p-cpu}  ")
# else:
#     print(f"lose game\t p:{p}\tcpu{cpu} ")


