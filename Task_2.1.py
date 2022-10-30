# 2 – Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from typing import Counter

numbers = input('Введите последовательность натуральных чисел: ')
list_numbers = [int(num) for num in numbers.split()]
no_reapets = list(set(numbers))
numbers_sorted = sorted(numbers)
numbers_unique = []
numbers_repeat = []
print(Counter(numbers_sorted))
for num, count in Counter(numbers_sorted).items():
    if count == 1:
        numbers_unique.append(num)
    else:
        numbers_repeat.append(num)

print(f'Исходная последовательность чисел: {list_numbers}')
print(f'Неповторяющиеся числа последовательности: {no_reapets}')
print(f'Повторяющиеся числа последовательсности: {numbers_repeat}')
print(f'Последовательность без повторяющихся чисел: {numbers_repeat}')
