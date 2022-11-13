from art import logo, vs
from game_data import data
import random
from replit import clear

def random_pick():
  pick = random.choice(data)
  return pick

#print(logo)
def play_game():
  print(logo)
  score = 0
  b = random_pick()
  keep_playing = True
  while keep_playing:
    a = b
    b = random_pick()
    if a["name"] == b["name"]:
      b = random_pick()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear()
    if (a["follower_count"] > b["follower_count"] and choice == 'A') or (b["follower_count"] > a["follower_count"] and choice == 'B'):
      score += 1
      print(f"You are right!   Current Score: {score}")
    else: 
      print(f"Sorry, that's wrong.   Final Score: {score}")
      keep_playing = False

play_game()