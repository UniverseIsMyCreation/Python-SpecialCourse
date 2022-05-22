import math

def degree(basement,num):
    coef = basement
    for i in range(num):
        basement *= coef
        if (basement == num):
            return True
        elif (basement > num):
            return False
    return False

def is_degree(num):
    upper_num = round(math.sqrt(num)) + 1
    for i in range(2,upper_num):
        if (degree(i,num)):
            return 'YES'
    return 'NO'

print(is_degree(int(input())))

"""
Какая-нибудь степень
Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли оно степенью натурального числа (>1). 
Вывести YES или NO соответственно.

Examples

    Input
        1024
    Output
        YES
"""