"""This code is to work on the lists"""

acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
print(acronyms)
print(acronyms[0])
print(acronyms[-1])
print(acronyms[0:2])
print(acronyms[0:2:1])

new_acronym = input("please input the acronym: ")
if new_acronym not in acronyms:
    acronyms.append(new_acronym)
    print(acronyms)
else:
    print("input acronym exists in list")

"""Print the items in the list one after the other in new lines"""

for acronym in acronyms:
    print(acronym)
