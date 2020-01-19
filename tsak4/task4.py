'''В течении дня в банк заходят люди, для каждого посещения фиксируется время захода в банк и время выхода. Банк работает с 8:00 до 20:00.
Написать программу, которая определяет периоды времени, когда в банке было максимальное количество посетителей. Файл содержит информацию о времени посещения банка каждым посетителем, округленном до минут. Время входа посетителя меньше либо равно времени выхода.
Выведите интервалы времени, когда в банке было максимальное число посетителей. Начало и конец интервала разделяются пробелом.
В случае необходимости вывести несколько периодов, в качестве разделителя между ними следует использовать символ перевода строки.'''
import datetime
import sys

'''Конвертирую масив строк в масив с форматом время часы и минуты'''
def time_convert (time_strings):
    time_str_tmp = []


    for time_part in time_strings:
        time_str_tmp.append(time_part.split(' '))
    j = 0
    datetime_arr = [[] for y in range(len(time_str_tmp))]
    for str_time in time_str_tmp:
        i = 0
        while i < 2:
            h, m = str_time[i].split(':')
            datetime_arr[j].append(datetime.time(int(h), int(m)).strftime('%H:%M'))
            i += 1
        j += 1
    return datetime_arr


time_strings = []
with open(sys.argv[1], 'r') as time_file:
    for time_l in time_file:
        time_strings.append(time_l.strip())

time_list = {}
converted_time = time_convert(time_strings)
for i in range(len(converted_time)):
    count = 0
    for j in range(len(converted_time)):
        if converted_time[j][0] <= converted_time[i][1] < converted_time[j][1]:
            count += 1
            time_list[str(converted_time[i][0]) +' '+ str(converted_time[j][1])] = count
max_val = max(time_list.values())

for key in time_list:
    if time_list[key] >= max_val:
        max_val = time_list[key]
        print(key)



