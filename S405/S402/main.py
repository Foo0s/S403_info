import requests
import json

#Вызов API
URL = "https://hacker-news.firebaseio.com/v0/item/1255326.json"
req = requests.get(URL)
print(req.status_code)

#Анализ структуры данных.
reqsponse_dict = req.json()

#Сохранение данных в файл.
with open("data_hacker.json", "w", encoding="UTF-8") as file:
    json.dump(reqsponse_dict, file, indent=4) #Запись в файл данных.