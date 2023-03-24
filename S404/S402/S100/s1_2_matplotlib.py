from s1 import Die
import random
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt

# Создание экземпляров кубика.
cub_1 = Die()
cub_2 = Die()

# Моделирование бросков.
list_1 = [cub_1.roll() + cub_2.roll() for i in range(1000)]

itog = [list_1.count(i) for i in range(2, (cub_1.cub + cub_2.cub) + 1)]
print(len(itog))
# Визуализация данных..
x_numbers = list(range(2, (cub_1.cub + cub_2.cub) + 1))
print(len(x_numbers))
# Визуализация данных Matplotlib..
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(x_numbers, itog, linewidth=6)

# Назначение заголовка диаграммы и осей
ax.set_title("Броски 2-ух кубов", fontsize=26)
ax.set_xlabel("Сумма костей", fontsize=16)
ax.set_ylabel("Количество выпадений", fontsize=16)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis="both", labelsize=16)

plt.show()
