password = input("Enter a password : ")
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","l","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char = ["@","!","#","$","%","&","?","/","."]
for i in password:
    if i in numbers:
        print("your password is weak")
        break
    elif i in numbers and i in letters:
        print("your password is good")
        break
    elif i in numbers and i in letters and i in char:
        print("your password is strong")
        break        