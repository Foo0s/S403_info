import requests
import json
from plotly import offline


def save_data():
    URL = "https://api.github.com/search/repositories?q=language:java&sort=stars"
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
    req = requests.get(URL, headers=headers)
    data = req.json()
    with open("data_java_statics.json", "w", encoding='UTF-8') as file:
        json.dump(data, file, indent=3)
    return data


def analitics(dt):
    # Сбор данных.
    name_rep, stars, id_rep, url, size = [], [], [], [], []
    for k in dt["items"]:
        name_rep.append(f"Название: {k['name']}<br />ID: {k['id']}<br />Ссылка: {k['url']}")
        stars.append(k['stargazers_count'])
        size.append(k['size'])
    return name_rep, stars, size


def visualisation(name, st, size):
    data = [{
        "type": "bar",
        "x": st,
        "y": size,
        "hovertext": name,
        "marker": {
            "color": "rgb(180, 70, 0)",
            "line": {"width": 2.2, "color": "rgb(210, 30, 14)"}
        },
        "opacity": 0.5  # Прозрачность
    }]

    my_layout = {"title": "Самые популярные репозитории на ЯП Java",
                 "titlefont": {"size": 30},
                 "xaxis": {"title": "Stars",
                           "titlefont": {"size": 22},
                           "tickfont": {"size": 18}
                           },
                 "yaxis": {"title": "Размер",
                           "titlefont": {"size": 22},
                           "tickfont": {"size": 18}
                           }
                 }

    fg = {"data": data, "layout": my_layout}
    offline.plot(fg, filename="java_analitics.html")


if __name__ == "__main__":
    a, b, c = analitics(save_data())
    visualisation(a, b, c)
