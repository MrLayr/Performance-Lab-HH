'''В магазине 5 касс, в каждый момент времени к кассе стоит очередь некоторой длины. Каждые 30 минут измеряется средняя длина очереди в каждую кассу (число с плавающей запятой) и для каждой кассы это значение записывается в соответствующий ей файл (всего 5 файлов).
Каждое значение заканчивается символом новой строки. Магазин работает 8 часов в день. Рассматривается только один день. На момент запуска приложения все значения уже находятся в файлах.
Написать программу, которая по данным замеров определяет интервал времени, когда в магазине было наибольшее количество посетителей за день.
Аргумент программы - путь к каталогу с файлами.
В каталоге будут 5 файлов: Cash1.txt, Cash2.txt ... Cash5.txt (Регистр имени важен!).'''
cash1_people = []
cash2_people = []
cash3_people = []
cash4_people = []
cash5_people = []

def largest_number_of_people (cash1, cash2, cash3, cash4, cash5):
    position = 0
    right_position = 0
    sum_of_people = cash1[0] + cash2[0] + cash3[0] + cash4[0] + cash5[0]
    while position < len(cash1):
        if sum_of_people < cash1[position] + cash2[position] + cash3[position] + cash4[position] + cash5[position]:
            sum_of_people = cash1[position] + cash2[position] + cash3[position] + cash4[position] + cash5[position]
            right_position = position
        position += 1
    return right_position + 1



with open('Cash1.txt', 'r') as cash1:
    for period1 in cash1:
        cash1_people.append(float(period1))
with open('Cash2.txt', 'r') as cash2:
    for period2 in cash2:
        cash2_people.append(float(period2))
with open('Cash3.txt', 'r') as cash3:
    for period3 in cash3:
        cash3_people.append(float(period3))
with open('Cash4.txt', 'r') as cash4:
    for period4 in cash4:
        cash4_people.append(float(period4))
with open('Cash5.txt', 'r') as cash5:
    for period5 in cash5:
        cash5_people.append(float(period5))

print(largest_number_of_people (cash1_people, cash2_people, cash3_people, cash4_people, cash5_people))
