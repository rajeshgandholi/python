"""This code is To calculate the expenses"""

# creating a list to add all the expenses

expenses = [10.50, 8, 5, 15, 20, 45, 67, 30]

sum = 0

for x in expenses:
    sum = sum + x

print("You spent: $", sum, sep='')
