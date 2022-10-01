# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
#
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def str_revers(str):
    count = len(str) - 1
    str_rev = ''
    for i in range(count+1):
        str_rev += str[count]
        count -= 1
    return str_rev


num_us = int(input('Введите число: '))
str_ = ''

while num_us >= 1:
    if num_us%2==1:
        str_ += '1'
    elif num_us%2==0:
        str_ += '0'
    num_us //=2

print('Данное число в двоичной системе равно:', str_revers(str_))