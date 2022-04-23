import matplotlib.pyplot as plt
import random as r

y = []
for i in range(200):
    y.append(r.randint(0, 150))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()  # добавляю диаграмму на картинку

ax.hist(y, 50)
ax.grid()
plt.show()

