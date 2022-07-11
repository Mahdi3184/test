num = int(input("\nEnter a number :  ")) # ye motaqayer sakhtim va adadi ra az karbar gerftim
if num < 0:#age adad kochek tar az 0 bashe
    print("sorry, factorial does not exist for negative numbers")#chap kon .......
else:# vgar na    
    factorial = 1 
    for i in range(1,num+1):# i dar base a 1 ta num+1
        factorial = factorial * i #  factorial * i kon briz toye  factorial
print(f"\nThe  factorial of {num} is : {factorial}") # chap kon.......       