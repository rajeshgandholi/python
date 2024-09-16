"""this code is to simulate the dice game between two players"""   # noqa
import random


# define the dice function
def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


# declare main function
def main():
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled:", roll1)
    print(player2, "rolled:", roll2)

    if (roll1 > roll2):
        print(player1, "WINS!!")
    else:
        print(player2, "WINS!!")


main()
