rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
list=[rock,paper,scissors]
list_size=len(list)
n=random.randint(0,list_size-1)


#computer input using random() function:
computer_choice=list[n]
print(computer_choice)

#user_input:
user_choice=int(input("Enter 0-for rock,1-for paper,2-for scissors: "))


#code if user choice was rock
if user_choice==0:
  user_choice=rock
  print(user_choice)
  if user_choice==rock and computer_choice==rock:
    print("Draw")
  elif user_choice==rock and computer_choice==paper:
    print("Computer Won")
  else:
    print("You Won")

    
#code if user choice was paper
elif user_choice==1:
  user_choice=paper
  print(user_choice)
  if user_choice==paper and computer_choice==paper:
    print("Draw")
  elif user_choice==paper and computer_choice==rock:
    print("You Won")
  else:
    print("Computer Won")

    
#code if user choice was scissors
else:
  user_choice=scissors
  print(user_choice)
  if user_choice==scissors and computer_choice==scissors:
    print("Draw")
  elif user_choice==scissors and computer_choice==rock:
    print("Computer Won")
  else:
    print("You Won")

print("Thanks For playing Rock,Paper,Scissor with me!!!!!")
