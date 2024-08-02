import random

art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

responses = ["r","p","s"]
response_names = ["rock","paper","scissors"]
who_won = ""

comp_choice = random.randint(0,2)
comp_art = art[comp_choice]

player_choice = input("Welcome to Rock, Paper, Scissors!\n"
                    "Type R for 'rock', P for 'paper', or S for 'scissors' to play.\n"
)

player_choice = responses.index(player_choice)
player_art = art[player_choice]

if player_choice == 0 and comp_choice == 2:
    who_won = "You won!"
elif player_choice == 2 and comp_choice == 0:
    who_won = "You lost!"
elif player_choice == 2 and comp_choice == 1:
    who_won = "You won!"
elif player_choice == 1 and comp_choice == 2:
    who_won = "You lost!"
elif player_choice == 1 and comp_choice == 0:
    who_won = "You won!"
elif player_choice == 0 and comp_choice == 1:
    who_won = "You lost!"
elif player_choice == comp_choice:
    who_won = "It's a draw!"

print(f"\nYou chose {response_names[player_choice]}.\n"
      f"{player_art}\n\n\n"
      f"The computer chose {response_names[comp_choice]}.\n"
      f"{comp_art}\n"
      f"{who_won}"
)