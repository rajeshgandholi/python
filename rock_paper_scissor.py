"""This is to create a game called Rock - Paper - Scissor"""
import random

"""line 5 to 17 is a hardcoded manner of rock paper scissor game"""

# computer_choice = 'scissors'
# user_choice = input(' Do you want rock, paper, or scissors?')

# if computer_choice == user_choice:
#     print("It's a TIE !!")
# elif user_choice == 'rock' and computer_choice == 'scissors':
#     print(' you WIN !!')
# elif user_choice == 'paper' and computer_choice == 'rock':
#     print(' you WIN !!')
# elif user_choice == 'scissors' and computer_choice == 'paper':
#     print(' you WIN !!')
# else:
#     print("you loose and computer WIN's !!")

"""line 21 to  is a hardcoded manner of rock paper scissor game"""

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input(' Do you want rock, paper, or scissors?')

if computer_choice == user_choice:
    print("It's a TIE !!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(' you WIN !!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(' you WIN !!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(' you WIN !!')
else:
    print("you loose and computer WIN's !!")
    print("The computer choose: " + computer_choice)
