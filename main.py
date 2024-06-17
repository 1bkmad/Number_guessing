#Number Guessing
import random
import os
art = '''
 ____   __ __  ___ ___  ____     ___  ____        ____  __ __    ___  _____ _____ ____  ____    ____ 
|    \ |  |  ||   |   ||    \   /  _]|    \      /    ||  |  |  /  _]/ ___// ___/|    ||    \  /    |
|  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )    |   __||  |  | /  [_(   \_(   \_  |  | |  _  ||   __|
|  |  ||  |  ||  \_/  ||     ||    _]|    /     |  |  ||  |  ||    _]\__  |\__  | |  | |  |  ||  |  |
|  |  ||  :  ||   |   ||  O  ||   [_ |    \     |  |_ ||  :  ||   [_ /  \ |/  \ | |  | |  |  ||  |_ |
|  |  ||     ||   |   ||     ||     ||  .  \    |     ||     ||     |\    |\    | |  | |  |  ||     |
|__|__| \__,_||___|___||_____||_____||__|\_|    |___,_| \__,_||_____| \___| \___||____||__|__||___,_|
  '''

def start_game():
  os.system("clear")
  print(art)
  number = random.randint(0,100)
  print("Welcome to the Number Guessing Game!!")
  print("I'm thinking of a nummber between 1 and 100.")
  chance = 0
  check=0
  while(check==0):
    difficulty=input("Choose a difficulty between \'easy\' and \'hard\' : ")
  
    if difficulty == 'easy':
      chance = 10
      check=1
    elif difficulty == 'hard' :
      chance = 5
      check=1
    else:
      print("choose correct difficulty")
  while(chance>0):
    print(f"You have {chance} number of attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    print(f"guess = {guess}")
    if guess > number:
      if guess - number >= 10:
        print("Guessed too high.")
      else:
        print("Guessed high but you are close!!")
      chance -= 1
    elif guess < number:
      if number-guess >= 10:
        print("Guessed too low.")
      else:
        print("Guessed low but you are close!!")
      chance -= 1
    else : 
      print(f"You got it!! The answer was {number}")
      break
  if chance == 0:
    print("You have run out of guesses, you lose.")
    print(f"The answer was {number}")
play_again='y'
while(play_again == 'y'):
  start_game()
  play_again=input("Press 'y' to play again ")
  
