"""This code is to define the class and the object functionality"""
"""We create a class same as function. Except a method has SELF as the first parameter"""   # noqa


class Robot_Dog:

    def __init__(self, name_val, breed_val) -> None:

        """
        Desc:    __init__ --> this method is to initialize the properties
                self is always the first parameter of init method
        Args:
                other parameters are the values that we want to initialize
        """
        self.name = name_val
        self.breed = breed_val

    def bark(self):
        print('Woof Woof!!')


# Main Program
my_dog = Robot_Dog('Spot', 'Chihuahua')
print(my_dog.name)
print(my_dog.breed)

my_dog.bark()
