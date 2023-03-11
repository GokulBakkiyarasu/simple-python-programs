from art import logo,vs
from game_data import data
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
def choose_data():
  return random.choice(data)

def statements(compare,follower):
  sentence=choose_data()
  for key in sentence:
    if key!="follower_count":
      if key=="name" or key=="description":
        compare += sentence[key]+", "
      else:
        compare += sentence[key]+"."
  for key in sentence:
    if key=="follower_count":
      follower+=sentence[key]
  return [compare,follower]

compare1=statements("Compare A: ",0)
should_continue=True
score=0
while should_continue==True:
  compare2=statements("Against B: ",0)
  if compare1[0]==compare2[0]:
      compare2=statements("Against B: ",0)  
  print(f"{compare1[0]}\n{vs}\n{compare2[0]}")
  guess=input("Who has more followers? Type 'A' or 'B':").lower()
  if guess=="a" and compare1[1]>compare2[1]:
    score+=1
    compare1=compare2
    n=str(compare1[0]).replace("Against B","Compare A")
    compare1[0]=n
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")
  elif guess=="b" and compare1[1]<compare2[1]:
    score+=1
    compare1=compare1
    n=str(compare1[0]).replace("Against B","Compare A")
    compare1[0]=n
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    should_continue=False
