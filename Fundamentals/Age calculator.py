"""This is to calculate the decades based on the age input."""

age = int(input('How old are you ?\n'))
decades = age // 10
years = age % 10
print(' you are '+ str(decades) + ' decades and '+ str(years) +' years old') # noqa2
