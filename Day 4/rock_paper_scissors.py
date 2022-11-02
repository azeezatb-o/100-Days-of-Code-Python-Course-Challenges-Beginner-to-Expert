import random
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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_input= int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
if user_input >= 3 or user_input < 0:
  print("You entered an invalid number. You lose!")
else:
  user_choice = game_images[user_input]
  print(f"You chose:\n{user_choice}")
  computer_input = random.randint(0, 2)
  computer_choice = game_images[computer_input]
  print(f"Computer chose:\n{computer_choice}")
  
  if user_input == computer_input:
    print("Its a draw!")
  elif user_input == 0 and computer_input == 2:
    print("You win!")
  elif computer_input == 0 and user_input == 2:
    print("You lose!")
  elif computer_input > user_input:
    print("You lose!")
  elif user_input > computer_input:
    print("You win!")

