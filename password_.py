from ntpath import join
from banar import banner
import random
import os
from colorama import Fore,init
import time

numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upeer_letter = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char = ["@","!","#","$","%","&","?","/",".",">","<"]
def ranPas():
    i = 0 
    while i <=8:
        global Create_password , Create_password_1
        Create_password_1 = []
        Create_password = random.choice(numbers,letters,upeer_letter,char)
        Create_password_1.append(join(Create_password))
        i += 1
ranPas()        
banner("login password","doom")
username = input("\nEnter a username : ")
def passw():
    global password , Selection
    print(Fore.CYAN+"\n{1}" , Fore.WHITE+"I make it myself")
    print(Fore.CYAN+"\n{2}" , Fore.WHITE+"make it yourself")
    Selection =  input("\nEnter the desired option : ")
    if Selection == "1":
        score = 0
        while True:
            password = input("\nEnter the password [must be 8 letters and include the number of small and capital letters and characters] : ")
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
    elif Selection == "2":
        ranPas()
        password ==  Create_password_1
        print(password)
passw()            
os.system("cls")
banner("login password","doom")
init()
print(Fore.GREEN + "\nyour information has been saved")
time.sleep(3)
os.system("cls")
banner("login password","doom")
def userPage():
    print(Fore.YELLOW + "\n{1}" , Fore.WHITE + "Change username")
    print(Fore.YELLOW + "\n{2}" , Fore.WHITE + "change password")
    change = input("\nEnter the desired option : ")
    if change == "1":
        changeUsername()
    elif change == "2":
        changePassword()
def changeUsername():
    global username
    os.system("cls")
    banner("login password","doom")
    new_username = input("\nEnter a new username :")
    username = new_username
    print(Fore.CYAN +"\nYour username has been successfully changed")
    os.system("cls")
    banner("login password","doom")
    login()
def changePassword():
    os.system("cls")
    banner("login password","doom")
    while True:
        last_password = input("\nEnter a your last password : ")
        if last_password == password:
            passw()
            new_password = input("\nRe-enter the new password : ")
            if new_password == password:
                print(Fore.CYAN + "\nYour password has been successfully changed")
                os.system("cls")
                banner("login password","doom")
                break
            elif new_password != password:
                print("\nThe password is wrong")
        elif last_password != password:
            print("\nThe password is wrong")
    login()
def login():
    global score_1
    score_1 = 0
    while True:
        if score_1 == 5:
            print(Fore.MAGENTA + "\nPlease search again after 10 seconds")
            time.sleep(10)
            score_1 = 0
        username_1 = input(Fore.WHITE +"\nEnter a your usernam : ")
        password_1 = input(Fore.WHITE +"\nEnter a your password : ")
        if username_1 == username and password_1 == password:
            os.system("cls")
            banner("login password","doom")
            time.sleep(1)
            print(Fore.CYAN+"\nWelcom to your account")
            break
        elif username_1 != username or password_1 != password:
            score_1 += 1
            print(Fore.RED +"\nThe username or password is incorrect")
    userPage()
login()


        

