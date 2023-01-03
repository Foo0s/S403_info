from s1 import Die
import random
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание экземпляров кубика.
cub_1 = Die()
cub_2 = Die()

# Моделирование бросков.
list_1 = [cub_1.roll() * cub_2.roll() for i in range(1000)]

itog = [list_1.count(i) for i in range(2, cub_1.cub + cub_2.cub)]

# Визуализация данных..
x_numbers = list(range(2, (cub_1.cub + cub_2.cub) + 1))
all = [Bar(x=x_numbers, y=itog)]
x_axis = {"title": "Грани куба", "dtick": 1}
y_axis = {"title": "Количество выпадений"}
diagramm = Layout(title="Результат выпадений двух восьмигранных кубов.",
                  xaxis=x_axis, yaxis=y_axis)

offline.plot({"data": all, "layout": diagramm}, filename="Statistika.html" )
