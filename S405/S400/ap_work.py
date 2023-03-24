import requests
import json

#Создание вызова API и сохранение ответа.

URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
req = requests.get(URL, headers=HEADERS)
print(req.status_code)

#Сохранение ответа API в переменной.
answer_serv = req.json()
with open("file_github_repositories2023.json", 'w') as f:
    json.dump(answer_serv, f, indent=4)

print(f"Всего репозиториев: {answer_serv['total_count']}")

#Анализ информации о репозиториях.
rep_dicts = answer_serv["items"]

print("Общая информация о репозитории: ")
for rep in rep_dicts:
    print(f"Ключи: {len(rep)}")
    print(f"Название репозитория: {rep['full_name']}")
    print(f"Владелец репозитория: {rep['owner']['login']}")
    print(f"Количество звезд, оценок репозитория: "
          f"{rep['stargazers_count']}")
    print(f"Сам репозиторий: {rep['html_url']}")
    print(f"Создано: {rep['created_at'][:10]}")
    print(f"Обновлено: {rep['updated_at'][:10]}")
    print(f"Описание репозитория: {rep['description']}")