"""This is to work on the loops functionality"""
# range --> this function has 3 parameters
#  parameter1: start
#  parameter2: stop
#  parameter3: step

print("---Printing inside the loop---")
for i in range(7):
    print(i)

total = 0
expenses = []

for i in range(7):
    expenses.append(int(input("Enter the expense: ")))

print("Your total expense is: $", sum(expenses), sep='')
