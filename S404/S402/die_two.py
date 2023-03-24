from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание кубика D7.

d_7 = Die()
d_7_two = Die()

# Моделирование серии бросков с сохранением результатов в списке.
num_list = []
for number in range(1000):
    result = d_7.roll() + d_7_two.roll()
    num_list.append(result)

# Анализ результатов.
itog = []
max_results = d_7.num_ug + d_7_two.num_ug
for value in range(2, max_results+1):
    itog_number = num_list.count(value)
    itog.append(itog_number)

# Визуализация результатов.
x_numbers = list(range(2, max_results + 1))
all = [Bar(x=x_numbers, y=itog)]
x_axis = {"title": "Грани куба", "dtick": 1}
y_axis = {"title": "Результат"}
my_diagramm = Layout(title="Результат выпадений граней 2-ух кубов - 1000 бросков",
                     xaxis=x_axis, yaxis=y_axis)

offline.plot({"data": all, "layout": my_diagramm}, filename="Thirst_d7_2.html")