import csv
import datetime
from matplotlib import pyplot as plt

filename = "death_valley_2018_simple.csv"

with open("../data/" + filename, "r", encoding="UTF-8") as file:
    f = csv.reader(file)
    header_all = next(f)

    hight_temp, low_temp, data = [], [], []
    for i in f:
        try:
            hight_temp.append(int(i[4]))
            low_temp.append(int(i[5]))
            data.append(datetime.datetime.strptime(i[2], "%Y-%m-%d"))
        except ValueError:
            print("Ошибка данных формата, число {}".format(data[-1]))


#Визуализация данных.
plt.style.use("seaborn")
fig, ax = plt.subplots()
title = "Температура Долины смерта на момент {} года".format(str(data[-1]).split("-")[0])
ax.plot(data, low_temp, c="purple", alpha=0.2)
ax.plot(data, hight_temp, c="yellow", alpha=0.89)
ax.fill_between(data, low_temp, hight_temp, facecolor="green", alpha=0.3)
plt.xlabel("Дата", fontsize=14)
plt.ylabel("Градусы, минимальные и максимальные.", fontsize=14)
plt.title(title, fontsize=16)
plt.show()