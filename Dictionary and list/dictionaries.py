"""This code is to work with dictionaries"""

"""Line 4 to 16 defines the usage of list and difficulty or maintaining it"""
"""Later this is replaced with dictionaries to make it easy"""

acronyms = ['LOL', 'TBD', 'WFH', 'WTH']
translations = ['laugh out loud', 'to be decided', 'work from home', 'what the hell'] # noqa

print("Printing acronyms list: ", acronyms)
print("Printing translations list: ", translations)

del acronyms[3]
del translations[3]

print("Printing latest acronyms list: ", acronyms)
print("Printing latest translations list: ", translations)


"""Below code is to replace list into dictionary"""

dic_acronyms = {
    'LOL': 'laugh out loud',
    'IDK': 'I dont know',
    'TBH': 'to be honest'
}

print("\n\nPrinting dictionary: ", dic_acronyms)
print("Printing LOL value from the dictionary: ", dic_acronyms['LOL'])  # noqa

del dic_acronyms['LOL']
print("Printing latest dictionary: ", dic_acronyms)


# the values to dictionary can also be added explicitly

dic_acronyms['TBD'] = 'to be decided'
print("Printing INSERTED dictionary: ", dic_acronyms)

# value in a dictionary can also be updated

dic_acronyms['TBD'] = 'decided'
print("Printing UPDATED dictionary: ", dic_acronyms)

# delete a key value from dictionary

del dic_acronyms['TBH']
print("Printing DELETED dictionary: ", dic_acronyms)

# looking for an unavailable key --> it returns an error
# print("Printing UN-AVAILABLE key from dictionary: ", dic_acronyms['BTW'])  # noqa

# overcome error when key is not available, instead return NONE type
print("Printing UN-AVAILABLE key from dictionary: ", dic_acronyms.get('BTW'))  # noqa


# best way to print a dictionary

definition = dic_acronyms.get('BTW')

if definition:
    print(definition)
else:
    print("key does not exist")


# example 1

sentence = 'IDK' + ' what is ' + 'TBD'
translation = dic_acronyms.get('IDK') + ' what is ' + dic_acronyms.get('TBD')  # noqa

print("\n", sentence, sep='')
print(translation)
