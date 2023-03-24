import csv
import matplotlib.pyplot as plt
def info_prcp():
    with open("../../data/death_valley_2018_simple.csv", "r", encoding="UTF-8") as f:
        file = csv.reader(f)
        header_text = next(file)

        info_pr = []
        for i in file:
            info_pr.append(float(i[3]))
    return info_pr

def visualisation():
    #Визуализация.
    plt.style.use("tableau-colorblind10")
    fig, ax = plt.subplots()
    ax.plot(info_prcp, c="yellow", alpha=0.9)
    plt.xlabel("Осадки", fontsize=22)
    plt.title("Осадки в Мертвой Долине (Пустыня)", fontsize=22)
    plt.show()