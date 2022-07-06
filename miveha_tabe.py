color_fruit = {"banana" : "yellow" , "cucumber" : "green" ,
"watermelon" : "red" , "blu-ray" : "blue" , "peach" : "pink" }

def pas():
    global password , password_1 
    password = 1234
    while True:
        password_1 =int(input("Enter a password:  "))
        if password_1 == password:
            print("\n your welcome")
            break
        else:
            print("\npassword not correct ")
pas()

def fruit():
    global fruits
    while fruits <=3:
        fruits = input("pleas enter a fruits name : ").lower()
        if fruits != color_fruit:
            print("choose one of the following fruits\n[banana,cucumber,watermelon,blu-ray,peach")
fruit()
for fruits in color_fruit:
    if fruits == color_fruit:
        print("The color of your fruit: " , color_fruit.values())
    elif fruits != color_fruit:
        print("error")    




    