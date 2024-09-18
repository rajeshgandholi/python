"""This is to practice on the exception handling"""

acronyms = {
    'LOL': 'laugh out loud',
    'IDK': 'I dont know',
    'TBH': 'to be honest'
}

# defs = acronyms['BTW']

# print('The program keeps going')
# the code breaks and above print command fails to execute due to line 9

try:
    defs = acronyms['LOL']
    print('Definition of ', acronyms, ' is ', defs)
except Exception:
    print('The key ', acronyms, " doesn't exists!")
finally:
    print('The acronyms we have defined are: ')
    for acronym in acronyms:
        print(acronym)
print('The program keeps going ....')
