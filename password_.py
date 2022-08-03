
import os
from colorama import Fore,init
import time

numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upeer_letter = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char = ["@","!","#","$","%","&","?","/",".",">","<"]
score = 0

while True:
    username = input("\nEnter a username : ")
    password = input("\nEnter a password : ")
    if len(password)>=8:
        for i in numbers:
            if i in password:
                score += 1
                break
        for i in letters:
            if i in password:
                score += 1
                break
        for i in upeer_letter:
            if i in password:
                score += 1
                break
        for i in char:
            if i in password:
                score += 1
                break
        if score  == 0:
            print("\nyour password is weak")
            score = 0
        elif score == 1:
            print("\nyour passwrd is weak")
            score = 0
        elif score == 2:
            print("\nyour password is almost good")
            score = 0 
        elif score == 3:
            print("\nyour password is good")
            score = 0
        elif score == 4:
            print("\nyour password is strong")
            break
    else:
        print("\nThe length of the string must be at least 8 characters")
os.system("cls")
init()
print(Fore.GREEN + "\nyour information has been saved")
time.sleep(3)
os.system("cls")
score_1 = 0
while True:
    if score_1 == 5:
        print(Fore.MAGENTA + "\nPlease search again after 10")
        time.sleep(10)
        score_1 = 0
    username_1 = input(Fore.WHITE +"\nEnter a your usernam : ")
    password_1 = input(Fore.WHITE +"\nEnter a your password : ")
    if username_1 == username and password_1 == password:
        os.system("cls")
        time.sleep(1)
        print(Fore.CYAN+"\nWelcom to your account")
        print(Fore.YELLOW + "\n{1}" , Fore.WHITE + "Change username")
        print(Fore.YELLOW + "\n{2}" , Fore.WHITE + "change password")
        change = input("\nEnter the desired option : ")
        if change == "1":
            os.system("cls")
            new_username = input("\nEnter a new username :")
            username = new_username
            print(Fore.CYAN +"\nYour username has been successfully changed")
        elif change == "2":
            os.system("cls")
            new_password = input(Fore.WHITE + "\nEnter a new password : ")
            password = new_password
            print(Fore.CYAN + "\nYour password has been successfully changed")
        break
    elif username_1 != username or password_1 != password:
        score_1 += 1
        print(Fore.RED +"\nThe username or password is incorrect")