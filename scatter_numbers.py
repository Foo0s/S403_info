import matplotlib.pyplot as plt

#Координаты
x_values = list(range(1, 100))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Greens, s=10) #Где s -> размер точки.

#Название осей, размеры.
ax.set_title("Точка на координате", fontsize=12)
ax.set_xlabel("Первая точка x", fontsize=24)
ax.set_ylabel("Первая точка y", fontsize=24)

#Размер шрифта и деления на оси.
ax.tick_params(axis="both", which="major", labelsize=12)

#Диапазон для каждой оси.
ax.axis([0, 100, 0, 11000])

plt.savefig("scatter_numbers.png", bbox_inches="tight")