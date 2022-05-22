in_circle = True
x,y,r = eval(input())
sqr = lambda y: y * y
while(True):
    a,b = eval(input())
    if (a == 0 and b == 0):
        break
    if (sqr(a - x) + sqr(b - y) <= sqr(r)):
        continue
    in_circle = False
if (in_circle):
    print('YES')
else:
    print('NO')

"""
Точки в круге
В первой строке ввести координаты центра круга и его радиус (числа x, y, r через запятую). 
Во второй и последующих строках ввести пары чисел — координаты точек. 
Ввод заканчивается парой 0,0 (она не входит в проверку!). 
Вывести YES, если все точки принадлежат кругу и NO, если не все.

Examples

    Input
        1,1,2
        1,2
        1,3
        2,2
        0,0
    Output
        YES
"""