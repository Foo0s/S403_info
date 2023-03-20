import random

class Random_walk():
    def __init__(self, num=5000):
        """Инициализирует начальное положение."""
        self.point = num

        #Положение.
        self.x_position = [0]
        self.y_position = [0]


    def random_move(self):
        """Генерация случайного блуждания."""
        while len(self.x_position) < self.point:
            self.x_move = random.choice([1, -1]) #Выбор направления.
            self.x_dist = random.choice([0, 1, 2, 3, 4, 5]) #Движение на задонное кол-во.
            self.result_x = self.x_move + self.x_dist

            self.y_move = random.choice([1, -1])
            self.y_dist = random.choice([1, -1])
            self.result_y = self.y_dist + self.y_move


            #Если нулевое значение.
            if self.result_x == 0 and self.result_y == 0:
                continue

            #Имуляция движения.
            self.x_d = self.x_position[-1] + self.result_x
            self.y_d = self.y_position[-1] + self.result_y

            #Добавление значений.
            self.x_position.append(self.x_d)
            self.y_position.append(self.y_d)

