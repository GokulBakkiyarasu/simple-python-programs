#python program for random bill pay generator
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
n=random.randint(0,(len(names)-1))
payer=names[n]
print(f"{payer} is going to buy the meal today!")
