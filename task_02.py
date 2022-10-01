# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def list_product_number(list):
    j = len(list) - 1
    list_product = []
    for i in range(j//2 + 1):
        list_product.append(i)
        list_product[i] = list[i] * list[j]
        j -= 1
    return list_product


list_0 = [2, 3, 4, 5, 6]
list_1 = [2, 3, 5, 6]

print(list_product_number(list_0))
print(list_product_number(list_1))
