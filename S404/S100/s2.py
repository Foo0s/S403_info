import matplotlib.pyplot as plt

y_numbers = list(range(1, 5000+1))
x_numbers = [x**3 for x in y_numbers]

#Использование стиля.
plt.style.use("ggplot")

#Подключение.
feg, ax = plt.subplots()
# ax.plot(y_numbers, x_numbers, c="orange", linewidth=1.3)

#Применение цветовой карты.
ax.scatter(y_numbers, x_numbers, c=x_numbers, cmap=plt.cm.Oranges)

#Название веток.
ax.set_title("Таблица 5000-кубов", fontsize=24)
ax.set_xlabel("Обычные числа", fontsize=16)
ax.set_ylabel("Кубы чисел", fontsize=16)

#Размер шрифта и делений оси.
ax.tick_params(axis="both", which='major', labelsize=6)

#Запуск
plt.show()

