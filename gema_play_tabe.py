def name():
    global player_1_name , player_2_name
    player_1_name = input("player_1 -> enter your name: ")
    player_2_name = input("player_2 -> enter your name: ")
name()
Score_player_1 = 0
Score_player_2 = 0
while Score_player_1 < 3 and Score_player_2 <3:
    print("\nenter 'end' to exit")
    player_1 = input("\nmake your move  [rock,paper,scissors] player_1: ").lower()
    player_2 = input("\nmake your move  [rock,paper,scissors] player_2: ").lower()
    if player_1 == "end" or player_2 == "end":
        print("gema over")
        break
    elif player_1 == player_2:
        print("\nthat's a tie")
    elif player_1 == "rock" and player_2 == "paper":
        print(f"\nThe {player_2_name} won")
        Score_player_2 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n{player_2_name} is :", Score_player_2)
    elif player_1 == "rock" and player_2 == "scissors":
        print(f"\nthe {player_1_name} won")
        Score_player_1 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n{player_2_name} is :", Score_player_2)
    elif player_1 == "paper" and player_2 == "rock":
        print(f"\nThe {player_1_name} won")
        Score_player_1 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n{player_2_name} is :", Score_player_2)
    elif player_1 == "paper" and player_2 == "scissors":
        print(f"\nThe {player_2_name} won")
        Score_player_2 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n{player_2_name} is :", Score_player_2)
    elif player_1 == "scissors" and player_2 == "rock":
        print(f"\nThe {player_2_name} won")
        Score_player_2 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n_{player_2_name} is :", Score_player_2)
    elif player_1 == "scissors" and player_2 == "paper":
        print(f"\nThe {player_1_name} won")
        Score_player_1 += 1
        print(f"\n{player_1_name} is :",Score_player_1)
        print(f"\n{player_2_name} is :", Score_player_2)
    else:
        print("\nplease enter one of these three")
if  Score_player_2 <  Score_player_1 :
    print(f"\nThe {player_1_name} won thes contest")
elif  Score_player_2 > Score_player_1:
    print(f"\nThe {player_2_name} won thes contest")
else:
    print("\nTher is no  winner in this contest")                   
