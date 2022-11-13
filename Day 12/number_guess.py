from art import logo
import random

EASY_NO_ATTEMPTS = 10
HARD_NO_ATTEMPTS = 5

def is_right(guess, answer, turns):
  if guess > answer:
    print("Too High \nGuess again")
    return turns - 1
  elif guess < answer:
    print("Too Low \nGuess again")
    return turns - 1
  else:
    print(f"You got it! The answer is {guess}")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_NO_ATTEMPTS
  else:
    return HARD_NO_ATTEMPTS


def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  random_number = random.randint(1, 100)

  turns = set_difficulty()

  
  guess = 0
  while guess != random_number:
    print(f"You have {turns} attempt(s) remaining to guess the number")
    guess = int(input("Make a guess: "))
    
    turns = is_right(guess, random_number, turns)

    if turns == 0:
      print(f"You have {turns} attempt(s) left, You lose")
      return 

play_game()
