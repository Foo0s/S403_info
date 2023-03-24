from random import randint

class Die():

    def __init__(self, num_ug=7):
        '''По умолчанию используется 7-ми гранный кубик.'''
        self.num_ug = num_ug

    def roll(self):
        '''Возвращает рандомное число от 1 до 7.'''
        return randint(1, self.num_ug)