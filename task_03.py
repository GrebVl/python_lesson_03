# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

list_ = []
size = 5

for i in range(size):
    list_.append(i)
    list_[i] = random.randrange(1000)/50


max_ = round(list_[0]%1, 2)
min_ = round(list_[0]%1, 2)

for j in range(size):
    if max_ < round(list_[j]%1, 2):
        max_ = round(list_[j]%1, 2)
    elif min_ > round(list_[j]%1, 2):
        min_ = round(list_[j]%1, 2)


print(list_)
print('Max = ', max_)
print('Min = ', min_)
print('Max - Min =', max_-min_)
