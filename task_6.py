# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 12
N = 6
a = []

print("В матрице:")
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print(f"{n:>5}", end="")
    a.append(b)
    print()

mx = -1

for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("максимальный элемент среди минимальных: ", mx)
