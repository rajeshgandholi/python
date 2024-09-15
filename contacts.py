"""Below code is to demo 'Parse a Nested Contacts Dictionary"""

contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Rajesh Sai', 'email': 'rajesh@example.com'},
        {'name': 'Sridhar', 'email': 'sridhar@example.com'},
        {'name': 'Teja', 'email': 'teja@example.com'},
        {'name': 'Sai Ram', 'email': 'sairam@example.com'}
    ]
}

print('----The students information----')
for students in contacts['students']:
    print(students)


print("\n----The students email id's information----")
for students in contacts['students']:
    print(students['email'])

print("\n---Printing the list defined inside a dictionary")
print(contacts['students'])
