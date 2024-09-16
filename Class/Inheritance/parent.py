class Robot:

    def __init__(self, name) -> None:
        self.name = name
        self.position = [0, 0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)

    def eat(self):
        print("I'm hungry!")
