import csv
import matplotlib.pyplot as plt

def down_file():
    """Выводит название станции, когда вводишь ссылку на нужный файл станции."""
    with open("../../data/sitka_weather_2018_simple.csv", "r", encoding="UTF-8") as f:
        file = csv.reader(f)
        headers = next(file)
        header_all = {n: i for i, n in enumerate(headers)}

        answer_station = []

        for i in header_all:
            if i == "STATION":
                number = header_all[i]
                while len(answer_station) == 0:
                    for i in file:
                        answer_station.append(i[number])
                        break
    return answer_station
print("Название станции: " + down_file()[0])

