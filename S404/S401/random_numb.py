#Импорт библиотек.

from random import choice

class RandomWalk():

    def __init__(self, num_points=5000):
        '''Инициализирует атрибут блуждания.'''
        self.number_points = num_points

        # Блуждания начинаются с коорд -> 0-0
        self.x_values = [0]
        self.y_values = [0]

    def get_walk(self):
        '''Расчет значений.'''

        # Определение направления и длины перемещения.
        self.x_direction = choice([1, -1, 0])  # движения вправо-влево.
        self.x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 12])  # дальность перемещения в этом направлении.

        self.y_direction = choice([1, -1, 0])
        self.y_distance = choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        '''Вычисляет все блуждания.'''

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.number_points:
            self.get_walk()

            x_step = self.x_direction * self.x_distance
            y_step = self.y_direction * self.y_distance

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление вследующих выражений x - y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)