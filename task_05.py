# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
# # - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num_us = int(input('Введите число k: '))

list_b = []

for i in range(num_us + 1):
    list_b.append(i)
    if i >= 2:
        list_b[i] = list_b[i - 1] + list_b[i - 2]


list_a = []

for j in range(num_us+1):
    list_a.append(j)
    list_a[j] = (-1)**(j + 1) * list_b[j]

list_a.pop(0)
list_a.reverse()

list_c = [*list_a, *list_b]

print(list_c)



