#!/usr/bin/env python3

# Program to play rock, paper, scissors

from os import system, name 
from random import randint
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Main
player_won = 0
computer_won = 0
while True:
	# dict to store player choices
	play = {}

	# imaginary player selects randomly
	comp = randint(1,3)
	if comp == 1:
		play['computer'] = 'rock'
	elif comp == 2:
		play['computer'] = 'paper'
	elif comp == 3:
		play['computer'] = 'scissor'
	print("Let's play!")
	print("1. Rock")
	print("2. Paper")
	print("3. Scissor")

	# user selects
	while True:
		print("Type 'exit' or 'quit' to leave.")
		choice = input("Your choice (1/2/3)...  ")
		if choice == 'exit' or choice == 'quit':
			print("\nYou Won:", str(player_won))
			print("I won  :", str(computer_won))
			if player_won == 0 and computer_won == 0:
				print("--> Overall Winner: None")
			elif player_won > computer_won:
				print("--> Overall Winner: You")
			elif player_won == computer_won:
				print("--> Overall Winner: None (Tie)")
			else:
				print("--> Overall Winner: Me")
			exit()

		if choice == '1':
			play['player'] = 'rock'
			break
		elif choice == '2':
			play['player'] = 'paper'
			break
		elif choice == '3':
			play['player'] = 'scissor'
			break
		else: 
			print("Please make sure you enter either '1' or '2' or '3'.\n")

	# Display entries:
	print("\nI chose  : ", play["computer"])
	print("You chose: ", play["player"])

	# check
	power = {'rock':1, 'paper':2, 'scissor':3,} 
	if play['computer'] == play['player']:
		print("--> It's a Tie.\n\n")
	else:
		c = power[play['computer']]
		p = power[play['player']]
		if p > c:
			res = p - c
			if res == 1:
				print("--> You Won.\n\n")
				player_won += 1
			else:
				print("--> You Lost.\n\n")
				computer_won += 1
		elif p < c:
			res = c - p
			if res != 1:
				print("--> You Won.\n\n")
				player_won += 1
			else:
				print("--> You Lost.\n\n")
				computer_won += 1

	# refresh 
	response = input("Press enter to proceed.")
	clear()
