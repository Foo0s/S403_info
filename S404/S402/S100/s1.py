from random import randint

class Die():

    def __init__(self, cub=8):
        self.cub = cub

    def roll(self):
        return randint(1, self.cub + 1)