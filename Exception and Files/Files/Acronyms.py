"""complete code of reading and writing to a file"""


def find_acronym():
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


def add_acronym():
    acronym = input('What acronym do you want to add? \n')
    definition = input('What is the definition? \n')
    with open('C:/Users/10695562/Personal/python/Exception and Files/Files/abbreviations.txt', 'a') as file:  # noqa
        file.write('\n' + acronym + ' - ' + definition)


def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    else:
        print("wrong choice!!")


main()
