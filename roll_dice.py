"""This is to create a code to randomly simulate the dice functionality"""

import random

# i = 0
# while (i < 6):
#     roll = random.randint(1, 6)
#     print('The computer rolled: ' + str(roll))
#     i += 1

"""Below code is to play a guess game with dice"""

roll = random.randint(1, 6)
guess = int(input('Guess the dice roll: '))

if (guess == roll):
    print(" correct! they rolled a " + str(roll))
else:
    print(" wrong !! computer rolled: " + str(roll))
