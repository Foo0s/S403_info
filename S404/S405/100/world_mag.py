import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

with open("../data/eq_data_30_day_m1.json", "r", encoding="UTF-8") as f2:
    file = json.load(f2)


with open("../data/eq_data_30.json", "w") as f3:
    json.dump(file, f3, indent=3)


#Чтение файла.
mag_all = [i["properties"]["mag"] for i in file["features"]]
x_cord = [j["geometry"]["coordinates"][0] for j in file["features"]]
y_cord = [k["geometry"]["coordinates"][1] for k in file["features"]]

#Нанесение данных на карту.
data = [{
    "type": "scattergeo",
    "lon": x_cord,
    "lat": y_cord,
    "marker": {
        "size": [i*7 for i in mag_all],
        "color": mag_all,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {
            "title": "Магнитуда"
        }
    }
}]

layout = Layout(title="Глобальные землетрясения")
all_dan = {"data": data, "layout": layout}
#Вывод.
offline.plot(all_dan, filename="world_map.html")