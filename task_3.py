# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random


def shaker_sort(array):

    left = 0
    right = len(array) - 1

    while left <= right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1

        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1

    return array


m = int(input("Введите натуральное число m: "))
array_new = [(random.randint(0, 100)) for _ in range(2 * m + 1)]
print("Исходный массив размером 2m + 1:\n", array_new)

print("Массив после сортировки:\n", shaker_sort(array_new))

print(f"Медиана массива равна: {array_new[int((2 * m + 1) / 2)]}")