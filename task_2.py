# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):

    if len(array) <= 1:
        return array

    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = array[:len(array)//2]
    right = array[len(array)//2:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while len(left) > i and len(right) > j:

        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while len(left) > i:
        array[k] = left[i]
        i += 1
        k += 1

    while len(right) > j:
        array[k] = right[j]
        j += 1
        k += 1
    return array


size = int(input("Введите количество элементов в массиве: "))
array_new = [round(random.uniform(0, 50), 2) for _ in range(size)]
print("Исходный массив:\n", array_new)

print("Конечный массив:\n", merge_sort(array_new))