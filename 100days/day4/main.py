import os
import random

os.system('cls')

#Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

#Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

#Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print('Your win!')
elif computer_choice > user_choice:
    print('You lose!')
elif computer_choice == user_choice:
    print("It's a draw!")
else:
    print("You typed an invalid number, you lose!")


