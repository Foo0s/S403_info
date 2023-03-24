import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

def geo_data(filename: str):
    """Функция, которая возвращает кол-во и значение землетрясений.
        Их местонахождение и время."""

    with open(filename, "r", encoding="UTF-8") as f:
        file = json.load(f)

    magnituda = [i["properties"]["mag"] for i in file["features"]]
    header = file["metadata"]["title"]
    place_mag = [y["properties"]["place"] for y in file["features"]]

    x_coordinate = [x["geometry"]["coordinates"][0] for x in file["features"]]
    y_coordinate = [y["geometry"]["coordinates"][1] for y in file["features"]]
    time = [t["properties"]["time"] for t in file["features"]]

    return magnituda, header, place_mag, x_coordinate, y_coordinate, time


def visualization(filename: str):
    """Функция, которая визуализирует информацию."""

    magn, header, place_mag, x_cord, y_cord, time = geo_data(filename)
    text = [f"{place_mag[i]}\nTime: {time[i]}" for i in range(len(place_mag))]

    data = [{
        "type": "scattergeo",
        "lon": x_cord,
        "lat": y_cord,
        "text": text,
        "marker": {
            "size": [m*3 for m in magn],
            "color": magn,
            "colorscale": "Cividis",
            "reversescale": True,
            "colorbar": {
                "title": "Магнитуда"
            }
        }
    }]

    layout = Layout(title="{}".format(header))
    programm = {"data": data, "layout": layout}
    return offline.plot(programm, filename="geo2023.html")

visualization("../data/significant_week.geojson.json")

