import matplotlib.pyplot as plt
import json


def read_json(f_name, key):
    dates = []
    prices = []
    with open(f_name) as jf:
        data = json.loads(jf.read())
        data = data['data']['rates']  # "очищаю" словарь от ненужных ключей
        for day in data:
            try:
                prices.append(data[day][key])  # добавляю количество продукта
                dates.append(day)  # добавляю день в список с днями
            except:
                pass
    return dates, prices


def make_plot(x_axis, y_axis, f_name, title='', x_label='', y_label='', color='#fc0303'):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    alias = list(range(0, len(x_axis), 10))  # "укорачиваю" список с днями
    plt.xticks(alias, rotation=45, fontsize=8)  # управляет подписями к осям диаграммы
    plt.grid()
    plt.plot(x_axis, y_axis, color=color, linewidth=3)
    plt.savefig(f'{f_name}.jpg')
    plt.savefig(f'{f_name}.pdf')
    plt.show()


dates, prices = read_json('series_SUGAR.json', 'SUGAR')
make_plot(dates, prices, 'sugar', 'Sugar prices', 'Dates', 'Prices', '#03fce7')
