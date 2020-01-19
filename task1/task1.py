'''Напишите программу, которая рассчитывает и подает в стандартный вывод следующие значения:
 90 перцентиль
 медиана
 максимальное значение
 минимальное значение
 среднее значение
Входные данные:
Данные для расчетов считываются из файла, путь к которому подается в виде аргумента. Числа в файле целые в пределах от -32 768 до 32 767. Каждое число с новой строки. В файле не более 1000 строк.'''
import sys
import math
''' для вычесления процентиля можно использовать библиотеку  numpy '''


def mediana (arr):
    '''проверяю четное ли количество элементо в вмасиве и исходя из этого считаю медиану'''
    if len(arr) % 2 != 0:
        return sorted(arr)[len(arr) // 2]
    else:
        return (sorted(arr)[len(arr) // 2 - 1] + sorted(arr)[len(arr) // 2]) / 2


def percentyl (arr, percent):
    size = len(arr)
    return sorted(arr)[int(math.ceil((size * percent) / 100)) - 1]


'''как вариант реализации функции нахождения минимального значения преведен ниже. По аналогии можно сделать нахождение максимального значения, но я воспользовался возможностями python'''
'''def min_vlue (arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min'''
file = open(sys.argv[1], 'r')
numbers = []

'получаю масив чисел из файла'
for line in file:
    numbers.append(int(line.strip()))

file.close()
print('%.2f' % percentyl(numbers, 90))
print('%.2f' % mediana(numbers))
print('%.2f' % max(numbers))
print('%.2f' % min(numbers))
print('%.2f' % (sum(numbers) / len(numbers)))





