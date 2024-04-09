import random

print("Let's play 5 rounds of rock, paper and scissors.")
score = 0
choices = ["rock", "paper", "scissors"]

for i in range(5):
    computer_choice = random.choice(choices)
    player_choice = input("What do you pick? rock/paper/scissors (case-sensitive): ")
    #draws
    if player_choice == computer_choice:
        print("It's a draw")
    #wins
    elif (player_choice == choices[0] and computer_choice == choices[2]) or \
         (player_choice == choices[1] and computer_choice == choices[0]) or \
         (player_choice == choices[2] and computer_choice == choices[1]):
        print("You won!")
        score += 1
    #losses
    else:
        print("You lost.")

print("You won " + str(score) + " out of 5 rounds.")