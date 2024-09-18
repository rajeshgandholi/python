#  Ask the user what acronym they want to add
#  Then ask the user for the definition
#  Open the file
#  Write the new acronym and definition to the file

acronym = input('What acronym do you want to add? \n')
definition = input('What is the definition? \n')
with open('C:/Users/10695562/Personal/python/Exception and Files/Files/abbreviations.txt', 'a') as file:  # noqa
    file.write('\n' + acronym + ' - ' + definition)
