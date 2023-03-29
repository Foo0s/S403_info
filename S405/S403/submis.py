import unittest

from plotly import offline
from operator import itemgetter
import requests
import json
import uni_t

URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(URL)
print(r)

file = r.json()


def info_user():
    all_users = []
    for i in range(1, 11):
        url = f"https://hacker-news.firebaseio.com/v0/item/{file[i]}.json"
        req = requests.get(url)
        file_two = req.json()
        user = {
            "name": file_two["by"],
            "parent": file_two["descendants"] if "descendants" in file_two else 0,
            "text": file_two["text"] if "text" in file_two else "none"
        }
        all_users.append(user)

    all_users = sorted(all_users, key=itemgetter("parent"), reverse=True)

    #Визуализация данных.
    data = [{
        "type": "bar",
        "x": [i['name'] for i in all_users],
        "y": [j['parent'] for j in all_users],
        "hovertext": [k['text'] for k in all_users],
        "marker": {
            "color": "rgb(10, 110, 210)",
            "line": {
                "width": 2.8, "color": "orange"
            },
        },
        "opacity": 0.8
    }]

    layout = {
        "title": "Популярные комментарии",
        "titlefont": {"size": 30, "color": "purple"},
        "xaxis": {"title": "Имена", "titlefont": {"size": 20, "color": "green"}, "tickfont": {"size": 20, "color": "red"}},
        "yaxis": {"title": "Количество комментариев", "titlefont": {"size": 20, "color": "rgb(1, 240, 90)"}, "tickfont": {"size": 20, "color": "rgb(90, 90, 120)"}}
     }

    fg = {"data": data, "layout": layout}
    offline.plot(fg, filename="analitics_commentaries.html")

if __name__ == '__main__':
    info_user()