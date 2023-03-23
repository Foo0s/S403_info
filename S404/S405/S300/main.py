import csv
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline
import datetime

def read_file(fi_name: str):
    """Функция, которая читает файл, возвращает значения:
        Дата, время, само происшествия и его место нахо-
        ждение."""

    with open(fi_name, "r", encoding="UTF-8") as f2:
        file = csv.reader(f2)
        header = next(file)
        for x,y in enumerate(header):
            print(x, y)
        print(header)

        #Широта и долгота.
        lat, long, data, br = [], [], [], []
        for x in file:
            lat.append(float(x[0]))
            long.append(float(x[1]))
            data.append(datetime.datetime.strptime(x[5], "%Y-%m-%d"))
            br.append(float(x[3]))
    return lat, long, data, br

def visual(filename: str):
    lt, ln, date, br = read_file(filename)
    data = [{
        "type": "scattergeo",
        "lon": ln,
        "lat": lt,
        "text": date,
        "marker": {
            "size": [i*2 for i in br],
            "color": br,
            "colorscale": "YlOrRd",
            "reversescale": False,
            "colorbar": {
                "title": "Пожары, баллы"
            }
        }
    }]
    m_lay = Layout(title="Пожары в мире. Количество.")
    all_info = {"data": data, "layout": m_lay}
    return offline.plot(all_info, filename="world_fire.html")

visual("../data/world_fires_1_day.csv")
