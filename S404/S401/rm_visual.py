# Импортирование...
import matplotlib.pyplot as plt

from random_numb import RandomWalk

# Построение случайного блуждания.
rw = RandomWalk()
rw.fill_walk()

# Нанесение точек на диаграмму.

# // Стиль.
plt.style.use("ggplot")

# // Подключение.
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=8)

# // Запуск.
plt.show()