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
print(f"Возвращенные репозитории: {len(rep_dicts)}")

#Анализ первого репозитория.
repo_dicts = rep_dicts[0]
print(f"Ключи: {len(repo_dicts)}")
print(f"Название репозитория: {repo_dicts['full_name']}")
print(f"Владелец репозитория: {repo_dicts['owner']['login']}")
print(f"Количество звезд, оценок репозитория: "
      f"{repo_dicts['stargazers_count']}")
print(f"Сам репозиторий: {repo_dicts['html_url']}")
print(f"Создано: {repo_dicts['created_at'][:10]}")
print(f"Обновлено: {repo_dicts['updated_at'][:10]}")
print(f"Описание репозитория: {repo_dicts['description']}")