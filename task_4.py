# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random

N = 21
a = []

for i in range(N):
    a.append(int(random() * 100))
print("В массиве:")
print(a)

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print(f"1-ый наименьший элемент № {min1 + 1}: {a[min1]}")
print(f"2-oй наименьший элемент № {min2 + 1}: {a[min2]}")
