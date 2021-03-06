import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    # reader() создает объект чтения данных для файла filename.
    reader = csv.reader(f)
    # next() возвращает следующую строку файла - в данном случае это заголовки.
    header_row = next(reader)

    # Чтение максимальной и минимальной температуры за каждый день перевод температуры из фаренгейт в цельсии
    # и добавление их в список.
    # Чтение даты с помощью strptime() переводит числа в дату формата год-месяц-день.
    highs, lows, dates = [], [], []
    for row in reader:
        high = round((int(row[5]) - 32) * 5 / 9)
        low = round((int(row[6]) - 32) * 5 / 9)
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

print(highs)
print(dates)

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(16, 9), dpi=128)
# Передача данных и изменение цвета линии на красный. парамерт alpha - прозрачность от 0 до 1.
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Закрашивает зону между двумя линиями по y. Принимает серию значений х и две сери по у.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы
plt.title('Daily high and low temperatures - 2014', fontsize=24)

# Даты еще не добавлены, поэтому метки по х остаются пустыми, но создать их необходимо.
plt.xlabel('', fontsize=16)

# Автоформатиование данных по оси х, чтобы надписи не перерывали друг друга.
fig.autofmt_xdate()

plt.ylabel('Temperature (C)', fontsize=16)
# Оформление делений на осях axis=both - к обеим осям х и у, which=major - к большим делениям(к малым = minor)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
