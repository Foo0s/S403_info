import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Изучение структуры данных.
filename = "../data/eq_data_1_day_m1.json"
with open(filename, "r", encoding="UTF-8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]
mag = [i["properties"]["mag"] for i in all_eq_dicts]
x_coordinate = [j["geometry"]["coordinates"][0] for j in all_eq_dicts]
y_coordinate = [y["geometry"]["coordinates"][1] for y in all_eq_dicts]

#Визуализация информации.

#data = [Scattergeo(lon=x_coordinate, lat=y_coordinate)] #Нанесение данных на карту.

#Другой способ
data = [{
    'type': 'scattergeo',
    'lon': x_coordinate,
    'lat': y_coordinate,
    'marker': {
        'size': [5*mags for mags in mag],
        },
    }]

my_layout = Layout(title="Землетрясения в мире")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_world_map.html")

