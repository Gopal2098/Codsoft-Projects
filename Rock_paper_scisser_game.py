
"""
#WORKFLOW OF THE PROJECT
1 - Input from the user(Rock,paper,Scissor)
2 - Complutor choice(computer will choose randomly not conditionly)
3 - result print


cases:
A- rock
rock - rock = tie
rock - paper = papper win
rock - scissor = rock win

B- paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

C- scissor
scissor - scissor =tie
scissor - rock = rock win
scissor - paper = scisser win


"""


import random
item_list = ["rock","paper","scissor"]

user_choice = input("Enter your move (rock, paper, scissor): ").strip().lower()
comp_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice not in item_list:
    print("Invalid input! Please choose rock, paper, or scissor.")
elif user_choice == comp_choice:
    print("Both chose the same: match tie")
elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers rock = computer wins")
    else:
        print("Rock smashes scissor = you win")
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Scissor cuts paper = computer wins")
    else:
        print("Paper covers rock = you win")
elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissor cuts paper = you win")
    else:
        print("Rock smashes scissor = computer wins")

# This code implements a simple Rock, Paper, Scissor game where the user plays against the computer.



