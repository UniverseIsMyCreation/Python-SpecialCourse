in_circle = True
str = input()
lst = str.split(',')
strtoint = lambda x: int(x)
sqr = lambda y: y * y
for i in range(len(lst)):
    lst[i] = strtoint(lst[i])
x,y,r = lst[0],lst[1],lst[2]
while(True):
    str = input()
    lst = str.split(',')
    for i in range(len(lst)):
        lst[i] = strtoint(lst[i])
    a,b = lst[0],lst[1]
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