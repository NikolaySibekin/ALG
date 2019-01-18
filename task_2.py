# Нахождение i-го по счету простого числа
# python -m timeit -n 100 -s "import task_1" "task_1.func_1(10000)"

import cProfile

qst = int(input("Введите, какое по счету простое число найти: "))
N = 1000

# вариант 1

primes = [2, 3]
last_crossed = [2, 3]


def fill_primes(N):
    while len(primes) < N:
        candidate = primes[-1] + 2
        i = 0
        while i < len(primes):
            while last_crossed[i] < candidate:
                last_crossed[i] += primes[i]
            if last_crossed[i] == candidate:
                candidate += 2
                i = 0
            i += 1

        primes.append(candidate)
        last_crossed.append(candidate)
    return primes

fill_primes(N)
print(f"{qst}-е по счету простое число (вариант 1): {primes[qst - 1]}")

#cProfile.run('fill_primes(10000)')
# 1    0.000    0.000    0.000    0.000 task_2.py:14(fill_primes) - 100
# 1    0.000    0.000    0.000    0.000 task_2.py:14(fill_primes) - 1000
# 1   29.345   29.345   34.943   34.943 task_2.py:14(fill_primes) - 10000

# вариант 2: решето Эратосфена

lst = [2]

def fill_eratosfen(N):
    for i in range(3, N + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

fill_eratosfen(N)
print(f"{qst}-е по счету простое число (вариант 2): {lst[qst - 1]}")

#cProfile.run('fill_eratosfen(10000)')
# 1    0.000    0.000    0.000    0.000 task_2.py:44(fill_eratosfen) - 100
# 1    0.001    0.001    0.001    0.001 task_2.py:44(fill_eratosfen) - 1000
# 1    0.010    0.010    0.010    0.010 task_2.py:44(fill_eratosfen) - 10000

# ВЫВОД: вариант 2 с решетом Эратосфена предпочтительнее, так как вычисляет простые числа быстрее.

