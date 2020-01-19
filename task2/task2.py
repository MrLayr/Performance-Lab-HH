import sys
'''
Напишите программу, которая определяет положение точки относительно выпуклого четырехугольника в двумерном пространстве.
Координаты фигуры считываются из файла №1. Это вершины четырехугольника, которые располагаются в порядке обхода фигуры по часовой стрелке.
Соответствия ответов:
0 - точка на одной из вершин 
1 - точка на одной из сторон 
2 - точка внутри 
3 - точка снаружи
'''
figure_dots_tmp = []
figure_dots = []
'получаю двуменрный масив строк c координами точек фигуры где [n][0] - x, а [n][1] - y'
with open(sys.argv[1], 'r') as file_figure:
    figure_dots_tmp.append(file_figure.read().split('\n'))
    for line in figure_dots_tmp[0]:
        figure_dots.append(line.split(' '))

dots_tmp = []
dots = []
'получаю масив строк c координами всех точек где [n][0] - x, а [n][1] - y'
with open(sys.argv[2], 'r') as file_dots:
    dots_tmp.append(file_dots.read().split('\n'))
    for line in dots_tmp[0]:
        dots.append(line.split(' '))

if 100 < len(dots_tmp) < 1:
    print("Количество точен должно быть от 1 до 100, выполнение алгоритма не возможно")
else:
    for dot in dots:
        if (float(dot[0]) < float(figure_dots[0][0]) or float(dot[1]) < float(figure_dots[0][1])) or (float(dot[0]) > float(figure_dots[2][0]) or float(dot[1]) > float(figure_dots[2][1])):
            print(3)
        elif(float(dot[0]) > float(figure_dots[0][0]) and float(dot[1]) >= float(figure_dots[0][1])) and (float(dot[0]) < float(figure_dots[2][0]) and float(dot[1]) <= float(figure_dots[2][1])):
            print(2)
        elif(float(dot[0]) == float(figure_dots[0][0]) and float(dot[1]) == float(figure_dots[0][1])) or (float(dot[0]) == float(figure_dots[1][0]) and float(dot[1]) == float(figure_dots[1][1])) or (float(dot[0]) == float(figure_dots[2][0]) and float(dot[1]) == float(figure_dots[2][1])) or (float(dot[0]) == float(figure_dots[3][0]) and float(dot[1]) == float(figure_dots[3][1])):
            print(0)
        elif(float(dot[0]) == float(figure_dots[0][0]) and float(dot[1]) < float(figure_dots[1][1])) or (float(dot[0]) < float(figure_dots[3][0]) and float(dot[1]) == float(figure_dots[0][1])) or (float(dot[0]) == float(figure_dots[2][0]) and float(dot[1]) < float(figure_dots[2][1])) or (float(dot[0]) < float(figure_dots[2][0]) and float(dot[1]) == float(figure_dots[2][1])):
            print(1)




