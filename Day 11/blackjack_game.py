import random
from replit import clear
from art import logo

#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rand_card = random.choice(cards)
  return rand_card


def calculate_score(test_cards):
  if len(test_cards) == 2 and sum(test_cards) == 21:
    return 0
  if sum(test_cards) > 21 and 11 in test_cards:
    test_cards.remove(11)
    test_cards.append(1)
  return sum(test_cards)

def compare(user_score, computer_score):
  if user_score == 0:
    return "You win with a blackjack"
  elif computer_score == 0:
    return "You lose. Opponent has a blackjack"
  elif user_score == computer_score:
    return "It's a draw"
  elif user_score > 21:
    return "You went over 21. You lose"
  elif computer_score > 21:
    return "Opponent went over 21. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  #user_cards = []
  #computer_cards = []
  #deal_card()
  print(logo)
  
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  go_on = True
  while go_on:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
                                   
    print(f"Your cards: {user_cards}, Your Current Score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    if user_score > 21 or user_score == 0 or computer_score == 0 :
      go_on = False
    
    more_card = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
    if more_card == 'n':
      go_on = False
      print("Game has ended")
    else:
      #deal_card()
      user_cards.append(deal_card())
  
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  compare(user_score, computer_score)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()