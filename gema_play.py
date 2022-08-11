import random
from banar import banner
import os
from colorama import Fore,init
init()
os.system("cls")
banner("r.p.s gema","doom")
print(Fore.YELLOW + "\n{1}", Fore.WHITE + "Game the system")
print(Fore.YELLOW + "\n{2}", Fore.WHITE + "Two player game")
Czech = input("\nEnter the desired option : ")
if Czech == "1":
    os.system("cls")
    banner("r.p.s gema","doom")
    nema = input("\nEnter a your nema : ")
    score_nema = 0
    score_system = 0
    list_1 =["rock","pepar","scissors"]
    while score_nema < 3 and score_system <3:
        system_1 =random.choice(list_1)
        print("\ntyap 'end' to exit")
        player = input("\nmake your move  [rock,paper,scissors] player_1: ").lower()
        if player == "end":
            print("gema over")
            break
        elif system_1 == player:
            print("\nthat's a tie")
        elif system_1 == "rock" and player == "paper":
            print(f"\nThe {nema} won")
            score_nema += 1
            print(f"\nsystem is :",score_system)
            print(f"\n{nema} is :", score_nema)
        elif system_1 == "rock" and player == "scissors":
            print(f"\nthe system won")
            score_system += 1
            print(f"\nsystem is :",score_system)
            print(f"\n{nema} is :", score_nema)
        elif system_1 == "paper" and player == "rock":
            print(f"\nThe system won")
            score_system+= 1
            print(f"\nsystem is :",score_system)
            print(f"\n{nema} is :", score_nema)
        elif system_1 == "paper" and player == "scissors":
            print(f"\nThe {nema} won")
            score_nema += 1
            print(f"\n{nema} is :",score_nema)
            print(f"\nsystem is :", score_system)
        elif system_1 == "scissors" and player == "rock":
            print(f"\nThe {nema} won")
            score_nema += 1
            print(f"\nsystem is :",score_system)
            print(f"\n_{nema} is :", score_nema)
        elif system_1 == "scissors" and player == "paper":
            print(f"\nThe system won")
            score_system += 1
            print(f"\nsystem is :",score_system)
            print(f"\n{nema} is :", score_nema)
        else:
            print("\nplease enter one of these three")
    if  score_nema <  score_system :
        print(f"\nThe system won thes contest")
    elif  score_nema> score_system:
        print(f"\nThe {nema} won thes contest")
    else:
        print("\nTher is no  winner in this contest")    
elif Czech == "2":
    os.system("cls")
    banner("r.p.s gema","doom")
    player_1_name = input("\nplayer_1 -> enter your name: ")
    player_2_name = input("\nplayer_2 -> enter your name:  ")
    Score_player_1 = 0
    Score_player_2 = 0
    while Score_player_1 < 3 and Score_player_2 < 3: 
        print("\ntyap 'end' to exit")
        player_1 = input("\nmake your move  [rock,paper,scissors] player_1: ").lower()
        player_2 = input("\nmake your move  [rock,paper,scissors] player_2 : ").lower()
        if player_1 == "end" or player_2 == "end":
            print("\ngame over")
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
               