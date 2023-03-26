import requests
from operator import itemgetter

URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
req = requests.get(URL) #Вызов
print(req.status_code)

submission = req.json()
print(submission)

users = []
for submis_id in submission[:20]:

    url = f"https://hacker-news.firebaseio.com/v0/item/{submis_id}.json"
    r = requests.get(url)
    #print(f"id: {submis_id}\nstatus code: {r.status_code}")

    response_dict = r.json()

    #Данные в словаре.

    user = {
        "title": response_dict["title"],
        "link": f"https://hacker-news.firebaseio.com/v0/item/{submis_id}.json",
        "comment": response_dict["descendants"] if "descendants" in response_dict else 0
    }

    users.append(user)

#Сортировка.
users = sorted(users, key=itemgetter("comment"), reverse=True)

for usr in users:
    print(f"title: {usr['title']}")
    print(f"link: {usr['link']}")
    print(f"comment: {usr['comment']}")
