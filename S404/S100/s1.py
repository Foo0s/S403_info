import matplotlib.pyplot as plt

y_numbers = list(range(1, 6))
x_numbers = [x**3 for x in y_numbers]

#Стиль графика.
plt.style.use("ggplot")

#Инициализация графика.
fig, ax = plt.subplots()
ax.plot(y_numbers, x_numbers, linewidth=3)

#Метки оси.Названия
ax.set_title("График кубов", fontsize=22)
ax.set_xlabel("Значения кубов", fontsize=16)
ax.set_ylabel("Обычные значения", fontsize=16)

#Размер шрифта и делений оси.
ax.tick_params(axis="both", which="major", labelsize=12)

#Запуск
plt.show()
