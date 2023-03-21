import csv
from matplotlib import pyplot as plt
from datetime import datetime

#Открытие файла
with open("../data/sitka_weather_07-2018_simple.csv", "r", encoding="UTF-8") as f1:
    read = csv.reader(f1)
    header_row = next(read) #Получение первой строки файла, содержащее заголовки.

    high_temp, data, low_temp = [], [], []
    #Чтение файла.
    for i in read:
        high_temp.append(int(i[5]))
        data.append(datetime.strptime(i[2], "%Y-%m-%d"))
        low_temp.append(int(i[6]))

#Нанесение данных на гистограмму.
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(33, 24))
fig.autofmt_xdate() #Наклоняет. Метки данных по диагонали.
ax.plot(data, high_temp, c="red") #Максимальная температура.
ax.plot(data, low_temp, c="blue") #Минимальная температура.

#Форматирование диграммы.
plt.title("Таблицы данных. Чтение данных, максимальная температура.")
plt.xlabel("Дата", fontsize=12)
plt.ylabel("Температура по Фаренгейту", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=18)

plt.show()

