# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array):

    position = 1

    while position < len(array):
        is_sorted = True

        for i in range(len(array) - position):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i +1], array[i]
                is_sorted = False

        if is_sorted:
            break

        position += 1

    return array


size = int(input("Введите количество элементов в массиве: "))
array_new = [(random.randint(-100, 99)) for _ in range(size)]
print("Исходный массив:\n", array_new)

print("Конечный массив:\n", bubble_sort(array_new))

