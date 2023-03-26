import json

import requests
from plotly.graph_objs import Bar
from plotly import offline

#Ссылка API
URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"} #Заголовки, необходимы для подтверждения.

#Создание запроса.
req = requests.get(URL, headers=HEADERS)

file = req.json()

#Создание файла, в который сохраняется json.
with open("apigithub.json", "w", encoding="UTF-8") as f:
    json.dump(file, f, indent=4)

#Общее количество найденных репозиториев с использованием ЯП Python.
all_repositories = file["total_count"]
#Имя репозитория, кол-во звёзд, участников.
all_stars_rep, labess, rep_links = [], [], []
for rep in file["items"]:
    name = rep["name"]
    url = rep["html_url"]
    rep_links.append(f"<a href='{url}'>{name}</a>")
    all_stars_rep.append(rep["stargazers_count"])
    labess.append(f"{rep['owner']['login']}<br />{rep['description']}")

#Построение графиков. Визуализация.
data = [{
    "type": "bar",
    "x": rep_links,
    "y": all_stars_rep,
    "hovertext": labess,
    "marker": {
        "color": "rgb(200, 70, 0)",
        "line": {"width": 2.5, "color": "rgb(90, 140, 120)"}
    },
    "opacity": 0.6
}]

my_layout = {
    "title": "Самые популярные репозитории на GitHub. ЯП - Python.",
    "xaxis": {"title": "Repository", "color": "blue", "titlefont": {"size": 24}, "tickfont": {"size": 14}},
    "yaxis": {"title": "Stars", "color": "orange", "titlefont": {"size": 24}, "tickfont": {"size": 14}}
}

fig = {"data": data, "layout": my_layout}

#Прогрузка. Визуализация.
offline.plot(fig, filename="github_analitics.html")
