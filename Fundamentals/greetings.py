"""This is to create a code that greets the person, who's name is passed as a parameter"""  # noqa


def greeting(name):
    print("Hello", name, "!!!", sep='\n')


#  Main program
input_name = input('Enter your name: ')
greeting(input_name)
