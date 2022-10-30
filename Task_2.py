# 32. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, список повторяемых 
# и убрать дубликаты из заданной последовательности.

from random import randint

def list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 8
m = 1
n = 10

origin = list(size, m, n)
print(origin)
print(get_unic_value(origin))
