import matplotlib.pyplot as plt
import random
from for_th import Random_walk

#Созд. экземпляра.
obj = Random_walk(5000)
obj.random_move() #Метод движения.

#Создание диаграммы.
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(15, 9)) #Размер экрана.
ax.plot(obj.x_position, obj.y_position, linewidth=2)

#Метки оси.
ax.set_title("Молекулярное движение",  fontsize=22) #Название таблицы.
ax.set_xlabel("Значения по оси x", fontsize=14)
ax.set_ylabel("Значения по оси y", fontsize=14)

#Размер шрифта и деление оси.
ax.tick_params(axis="both", which="major", labelsize=8)
plt.show()



