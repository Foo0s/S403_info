# Импортирование...
import matplotlib.pyplot as plt
import random

from random_numb import RandomWalk

# Генерирование новых блужданий.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk(random.randint(5000, random.randint(5001, 50000)))
    rw.fill_walk()

    # Нанесение точек на диаграмму.

    # // Стиль.
    plt.style.use("ggplot")

    # // Подключение.
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.number_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges,
               edgecolors="none", s=2.7)      # edgecolors -> удаление черного контура.

    # // Вывод первой точки.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='blue', edgecolors="green", s=101)

    # // Вывод последней точки.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="green", edgecolors="blue", s=101)

    # // Удаление осей.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # // Запуск.
    plt.show()

    stop_running = input("Остановка - ?: \n(y/n): ")
    if stop_running.lower() == "n":
        print("Блуждание окончилось.")
        break
    else:
        continue