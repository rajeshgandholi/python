from parent import Robot


class Robot_Dog(Robot):
    """This notation of passing 'Robot' class as a parameter is called inheritance"""   # noqa
    """by default if there is no __init__ method created here, so it invokes the __init__ method of the parent class 'Robot'"""   # noqa

    def make_noise(self):
        print('Woof Woof !!')

    def eat(self):  # this is used to override the method created in parent class, where the child method is called rather than parent method  # noqa
        super().eat()   # super() method helps to invoke the parent class method   # noqa
        print("I like bacon!")


my_robot_dog = Robot_Dog('Bud')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()
