with open('C:/Users/10695562/Personal/python/Exception and Files/Files/abbreviations.txt') as file:   # noqa
    result = file.read()
    print(result)

    result1 = file.readlines()
    print('-----------------------------')
    print(result1)
#  read(): this method reads the file and return the content of the file
#  readlines(): this method return the list of strings of all the lines in the file  # noqa


# There is an alternative for line 5
with open('C:/Users/10695562/Personal/python/Exception and Files/Files/abbreviations.txt') as files:  # noqa
    for line in files:
        print(line)
