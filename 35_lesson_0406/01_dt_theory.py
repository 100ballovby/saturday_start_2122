from datetime import datetime, timedelta


today = datetime.today()
print(today)
summer_start = datetime(year=2022, month=6, day=1)  # 1.06.2022
summer_end = datetime(year=2022, month=8, day=31)  # 31.08.2022
delta = summer_end - summer_start
print(delta)

# посчитать число, которое будет через несколько дней
from_5_days = today + timedelta(days=8)
print(datetime.strftime(from_5_days, '%d.%m.%y'))

# достанем отдельные элементы
if today.hour >= 13 and today.weekday() in [5, 6]:
    # если сейчас больше 13 часов и сегодня суббота или воскресенье
    print('Мы не работаем, приходите завтра!')
else:
    print('добро пожаловать!')