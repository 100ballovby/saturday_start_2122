import matplotlib.pyplot as plt

values = [10, 45, 36, 71, 14, 6]
labels = ['BMW', 'Mercedes', 'Fiat', 'Audi', 'Porsche', 'Bugatti']
plt.title('Auto brands market')
plt.pie(values, labels=labels, autopct='%.2f', radius=1.2,
        wedgeprops=dict(width=0.6))
plt.show()

