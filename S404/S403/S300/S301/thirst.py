import csv
from matplotlib import pyplot as plt
from datetime import datetime

def info_prcp():
    with open("../data/sitka_weather_2018_simple.csv", "r", encoding="UTF-8") as file:
        f = csv.reader(file)
        header_all = next(f)

        info_pr = []
        #Извлечение данных.
        for k in f:
            info_pr.append(float(k[3]))
    return info_pr

def visualization(info_prcp):
    #Визуализация данных.
    plt.style.use("grayscale")
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.plot(info_prcp, c="orange")
    plt.xlabel("Кол-во осадков", fontsize=16)
    plt.title("Осадки в городе Ситка.", fontsize=22)
    plt.show()

object = info_prcp()
visualization(object)