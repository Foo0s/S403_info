import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
import thirst, two

a = thirst.info_prcp()
b = two.info_prcp()
while len(a) != len(b):
    if len(a) > len(b):
        del a[-1]
    else:
        del b[-1]

#Визуализация данных.
# plt.style.use("bmh")
# fig, ax = plt.subplots()
# ax.plot(a, c="red", alpha=0.5)
# ax.plot(b, c="black", alpha=0.6)
# ax.fill_between(a, b, facecolor="orange", alpha=0.3)
# plt.title("Разница осадков В г. Ситка и в пустыне Мертвая Долина", fontsize=20)
# plt.xlabel("Осадки", fontsize=16)
# plt.show()

#Общее количество осадков за год.
lst = []
lst.append(sum(a))
lst.append(sum(b))

plt.style.use("bmh")
fig, ax = plt.subplots(figsize=(30, 20))
data = [Bar(x=a, y=lst)]
x_axis = {"title": "Кол-во осадков в разных местностях"}
y_axis = {"title": "Значения"}
my_layout = Layout(title="ОСАДКИ", xaxis=x_axis, yaxis=y_axis)
offline.plot({"data": data, "layout": my_layout}, filename="ocadk.html")
