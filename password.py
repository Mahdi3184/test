numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upeer_letter = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char = ["@","!","#","$","%","&","?","/","."]

while True:
    password = input("\nEnter a password : ")
    if len(password)>=8:
        for i in numbers and letters and upeer_letter and char:
            if i in password:
                print("\nyour password is strong")
                break
        for i in numbers :
            if i in password :
                print("\nyour password is weak")
                break
        for i in letters and upeer_letter:
            if i in password:
                print("\nyour password is weak")
                break
        for i in letters and upeer_letter and numbers:
            if i in password:
                print("\nyour password is good")
                break
    else:
        if len(password)<=8:
            print("\nThe length of the string must be at least 8 characters")
 