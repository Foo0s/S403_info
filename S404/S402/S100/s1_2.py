from s1 import Die
import random
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание экземпляров кубика.
cub_1 = Die()
cub_2 = Die()

# Моделирование бросков.
list_1 = []
for i in range(1000):
    result = cub_1.roll() * cub_2.roll()
    list_1.append(result)

itog = []
max_numbers = cub_1.cub + cub_2.cub
for i in range(2, max_numbers + 1):
    value_number = list_1.count(i)
    itog.append(value_number)

# Визуализация данных..
x_numbers = list(range(2, max_numbers + 1))
all = [Bar(x=x_numbers, y=itog)]
x_axis = {"title": "Грани куба", "dtick": 1}
y_axis = {"title": "Количество выпадений"}
diagramm = Layout(title="Результат выпадений двух восьмигранных кубов.",
                  xaxis=x_axis, yaxis=y_axis)

offline.plot({"data": all, "layout": diagramm}, filename="Statistika.html" )
