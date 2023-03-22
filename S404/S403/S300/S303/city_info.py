import csv
import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline

def open_file(file_name: str):
    """Функция, которая открывает файл, и возвращает обработанные данные с неё."""
    with open(file_name, "r", encoding="UTF-8") as f:
        file = csv.reader(f)
        header = next(file)

        wsf5 = [i[24] for i in file]
    print(wsf5)
    return wsf5


answer = open_file("../../data/American_citi.csv")
plt.style.use("bmh")
fig, ax = plt.subplots(figsize=(30, 20))
data = [Bar(x=answer)]
x_ax = {"title": "Параметр", "dtick": 2}
y_ax = {"title": "Параметр", "dtick": 4}
layout = Layout(title="Данные с города Sacramento", xaxis=x_ax, yaxis=y_ax)
offline.plot({"data": data, "layout": layout}, filename="sacramento.html")

