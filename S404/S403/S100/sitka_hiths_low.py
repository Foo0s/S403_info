from matplotlib import pyplot as plt
from datetime import datetime
import csv

#Чтение файла.
with open("../data/sitka_weather_07-2018_simple.csv", "r", encoding="UTF-8") as file:
    f = csv.reader(file)
    header_file = next(f)

    #Списки, хранение данных.
    low_temp, max_temp, data = [], [], []
    #Достаю информацию из файла..
    for i in f:
        low_temp.append(int(i[6]))
        max_temp.append(int(i[5]))
        data.append(datetime.strptime(i[2], "%Y-%m-%d"))

#Визуализация данных.
plt.style.use("seaborn") #Использование стиля.
fig, ax = plt.subplots()

# ax.plot(data, low_temp, c="blue")
# ax.plot(data, max_temp, c="red")

"""Цветовое выделение части диаграммы."""
ax.plot(data, low_temp, c="orange", alpha=0.5)
ax.plot(data, max_temp, c="yellow", alpha=0.5)
plt.fill_between(data, low_temp, max_temp, facecolor="blue", alpha=0.1)
plt.title("Второй график данных о погоде")
plt.show()