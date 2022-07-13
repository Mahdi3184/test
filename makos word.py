from os import renames


sentence = input("pleas enter a sentence (3 words or more): ")
new_sentence = sentence.split(" ")
makos_sentence =[]
for i in new_sentence:
     makos_sentence.append(i[::-1])    
words = len(new_sentence)
i = 0 
my_dict = {}
while i < words:
    my_dict[new_sentence[i]] = makos_sentence[i]
    i =+1
print(my_dict)
print(" ".join(makos_sentence))    



# print(makos_sentence)    
