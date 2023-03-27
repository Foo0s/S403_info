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
        url.append(f"<a href='{k['url']}'>{k['name']}</a>")
    return name_rep, stars, size, url


def visualisation(name, st, size, ur):
    data = [{
        "type": "bar",
        "x": ur,
        "y": st,
        "hovertext": name,
        "marker": {
            "color": "rgb(180, 70, 0)",
            "line": {"width": 2.2, "color": "rgb(210, 30, 14)"}
        },
        "opacity": 0.5  # Прозрачность
    }]

    my_layout = {"title": "Самые популярные репозитории на ЯП Java",
                 "titlefont": {"size": 30, "color": "rgb(123, 50, 23)"},
                 "xaxis": {"title": "Stars",
                           "titlefont": {"size": 22, "color": "rgb(220, 50, 0)"},
                           "tickfont": {"size": 18, "color": "yellow"}
                           },
                 "yaxis": {"title": "Размер",
                           "titlefont": {"size": 22, "color": "rgb(130, 50, 21)"},
                           "tickfont": {"size": 18, "color": "orange"}
                           }
                 }

    fg = {"data": data, "layout": my_layout}
    offline.plot(fg, filename="java_analitics.html")


if __name__ == "__main__":
    a, b, c, d = analitics(save_data())
    visualisation(a, b, c, d)
