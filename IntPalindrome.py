def is_palindrome(num):
    origin = num
    temp_num = 0
    while (num != 0):
        temp_num = temp_num * 10 + (num % 10)
        num //= 10
    if (temp_num == origin):
        return 'YES'
    else:
        return 'NO'

print(is_palindrome(int(input())))

"""
Число-палиндром
Ввести целое положительное число и проверить, является ли оно палиндромом, 
т. е. совпадает ли первая цифра с последней, вторая — с предпоследней и т. д. 
Представлять число в виде последовательности (строки, списка и т. п.) нельзя. 
Вывести YES или NO соответственно. Лидирующие нули не учитывать (числа, заканчивающиеся на 0 — автоматически не палиндромы).

Examples

    Input
        1234321
    Output
        YES
"""