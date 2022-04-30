import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # seaborn - надстройка над matplotlib

filename = 'bestsellers_with_categories_2022_03_27.csv'
table = pd.read_csv(filename)  # Открыть прочитать таблицу
print(table.head())

plt.figure(figsize=(15, 7))
sns.lineplot(x='Year', y='Price',
             palette='mako_r',
             hue='Genre', data=table).set(title='Book prices by Genre (2009-2022)')
plt.savefig('prices.jpg')
plt.show()

