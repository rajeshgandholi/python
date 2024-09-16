"""Here we will look into the list vs dictionary"""
"""Also we will see the 2D list vs dictionary of lists"""

# 2D list

menus = [
    ['Egg Sandwich', 'Idly', 'Dosa'],
    ['Rice', 'Beans', 'Chicken'],
    ['Roti', 'Kurma', 'Salad']
]

# running print command on 1D basis
print('Printing menu on 1D basis: ')
print(menus[0])
print(menus[1])
print(menus[2])

# running print command on 2D basis
print('\nPrinting menu on 2D basis: ')
print(menus[0][0])
print(menus[1][1])
print(menus[2][2])


"""Above declared 2D list can be converted into a DICTIONARY"""

dic_menu = {
    "Breakfast": ['Egg Sandwich', 'Idly', 'Dosa'],
    "Lunch": ['Rice', 'Beans', 'Chicken'],
    "Dinner": ['Roti', 'Kurma', 'Salad']
}

print("\n----Printing from the dictionary----")
print("\nPrinting BREAKFAST menu from the dictionary: ", dic_menu.get('Breakfast'))  # noqa
print("\nPrinting LUNCH menu from the dictionary: ", dic_menu.get('Lunch'))
print("\nPrinting DINNER menu from the dictionary: ", dic_menu.get('Dinner'))


# to loop over the dictionary and fet KEY along with the VALUES

print("\n----Printing dictionary using a LOOP----")
for name, menu in dic_menu.items():  # items() --> this method helps to fetch both key and value  # noqa
    print(name, ':', menu)
