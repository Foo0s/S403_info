import matplotlib.pyplot as plt
import thirst, two

a = thirst.info_prcp()
b = two.info_prcp()
while len(a) != len(b):
    if len(a) > len(b):
        del a[-1]
    else:
        del b[-1]

#Визуализация данных.
plt.style.use("bmh")
fig, ax =
print(len(a), len(b))