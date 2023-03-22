import csv
import matplotlib.pyplot as plt
import datetime

with open("../../data/Atlanta.csv", "r", encoding="UTF-8") as f:
    file = csv.reader(f)
    headers = next(file)

    tmax, tmin, data = [], [], []
    for i in file:
        tmax.append(int(i[11]))
        tmin.append(int(i[12]))
        data.append(datetime.datetime.strptime(i[5], "%Y-%m-%d"))

#Visualisation.
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(23, 23))
plt.title("Разница погоды мин-макс в Атланте.", fontsize=20, c="orange")
plt.xlabel("Дата", fontsize=14)
plt.ylabel("Градусы", fontsize=14)
plt.plot(data, tmax, c="orange", alpha=0.9)
plt.plot(data, tmin, c="yellow", alpha=1)
plt.tick_params(axis="both", which="major")
plt.fill_between(data, tmax, tmin, facecolor="blue", alpha=0.4)
plt.show()
