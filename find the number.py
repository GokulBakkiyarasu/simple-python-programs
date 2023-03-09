logo="""

//     ____    _   _U _____ u____   ____          _____   _   _ U _____ u      _   _      _   _  __  __    ____ U _____ u  ____     
//  U /"___|U |"|u| \| ___"|/ __"| / __"| u      |_ " _| |'| |'|\| ___"|/     | \ |"|  U |"|u| U|' \/ '|U | __")\| ___"|U |  _"\ u  
//  \| |  _ /\| |\| ||  _|"<\___ \<\___ \/         | |  /| |_| |\|  _|"      <|  \| |>  \| |\| \| |\/| |/\|  _ \/|  _|"  \| |_) |/  
//   | |_| |  | |_| || |___ u___) |u___) |        /| |\ U|  _  |u| |___      U| |\  |u   | |_| || |  | |  | |_) || |___   |  _ <    
//    \____| <<\___/ |_____||____/>|____/>>      u |_|U  |_| |_| |_____|      |_| \_|   <<\___/ |_|  |_|  |____/ |_____|  |_| \_\   
//    _)(|_ (__) )(  <<   >> )(  (__)(  (__)     _// \\_ //   \\ <<   >>      ||   \\,-(__) )( <<,-,,-.  _|| \\_ <<   >>  //   \\_  
//   (__)__)    (__)(__) (__(__)   (__)         (__) (__(_") ("_(__) (__)     (_")  (_/    (__) (./  \.)(__) (__(__) (__)(__)  (__) 


"""
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard': ")
real_number=random.randint(1,100)
def game():
  def hard():
    if difficulty_level=="hard":
      moves=5
      print(f"You have {moves} attempts remaining to guess the number.")
      while moves>0 and moves<=5:
        guess_number=int(input("Make a guess: "))
        if moves>1:
         if guess_number>real_number:
          print("Too high.\nGuess again.")
          moves-=1
          print(f"You have {moves} attempts remaining to guess the number.")
         elif guess_number<real_number:
          print("Too low.\nGuess again.")
          moves-=1
          print(f"You have {moves} attempts remaining to guess the number.")
         elif guess_number==real_number:
          print(f"You got it! The answer was {guess_number}")
          moves=0
         else:
          print("You've run out of guesses, you lose.")
        else:
          if guess_number==real_number:
           print(f"You got it! The answer was {guess_number}")
           moves=0
          else:
           print("You've run out of guesses, you lose.")
           moves-=1
  def easy():
    if difficulty_level=="easy":
      moves=10
      print(f"You have {moves} attempts remaining to guess the number.")
      while moves>0 and moves<=10:
        guess_number=int(input("Make a guess: "))
        if moves>1:
         if guess_number>real_number:
          print("Too high.\nGuess again.")
          moves-=1
          print(f"You have {moves} attempts remaining to guess the number.")
         elif guess_number<real_number:
          print("Too low.\nGuess again.")
          moves-=1
          print(f"You have {moves} attempts remaining to guess the number.")
         elif guess_number==real_number:
          print(f"You got it! The answer was {guess_number}")
          moves=0
         else:
          print("You've run out of guesses, you lose.")
        else:
          if guess_number==real_number:
           print(f"You got it! The answer was {guess_number}")
           moves=0
          else:
           print("You've run out of guesses, you lose.")
           moves-=1
  if difficulty_level=="hard":
    hard()
  elif difficulty_level=="easy":
    easy()
  else:
    print("Enter proper difficulty level")
game()

  
