from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание кубика D7.

d_7 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
num_list = []
for number in range(1000):
    result = d_7.roll()
    num_list.append(result)

# Анализ результатов.
itog = []
for value in range(1, d_7.num_ug+1):
    itog_number = num_list.count(value)
    itog.append(itog_number)

# Визуализация результатов.
x_numbers = list(range(1, d_7.num_ug + 1))
all = [Bar(x=x_numbers, y=itog)]
x_axis = {"title": "Грани куба"}
y_axis = {"title": "Результат"}
my_diagramm = Layout(title="Результат выпадений граней кубика - 1000 бросков",
                     xaxis=x_axis, yaxis=y_axis)

offline.plot({"data": all, "layout": my_diagramm}, filename="Thirst_d7.html")