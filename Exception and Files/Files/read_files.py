"reading and writing files"

#  open a file
#  read a file
#  ask user input to search for an acronym

look_up = input('What software acronym would you like to look up? ')


found = False
with open('C:/Users/10695562/Personal/python/Exception and Files/Files/abbreviations.txt') as file:  # noqa
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print('The acronym does not exist!!')
