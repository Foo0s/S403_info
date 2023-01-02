import matplotlib.pyplot as plt

begin_number = [2, 3, 4, 5, 6]
numbers = [4, 9, 16, 25, 36]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(begin_number, numbers, linewidth=3)

#Назначение заголовка диграммы и меток осей.
ax.set_title("Квадраты чисел", fontsize=16)
ax.set_xlabel("Числа", fontsize=12)
ax.set_ylabel("Квадраты", fontsize=16)

#Назначение размера шрифта делений на осях.
ax.tick_params(axis="both", labelsize=14)

plt.show()