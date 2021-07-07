# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# python -m timeit -n 100 -s "import task_1" "task_1.func_1(10000)"

import cProfile

qnt = int(input("Сколько элементов сложить: "))

# вариант 1


def func_1(n):
    item = 1
    sum_ = 0
    for _ in range(n):
        sum_ += item
        item /= -2
    return sum_

# 100 loops, best of 5: 1.45 msec per loop - 10000
# 100 loops, best of 5: 14.3 msec per loop - 100000
# 100 loops, best of 5: 145 msec per loop - 1000000
# 100 loops, best of 5: 1.48 sec per loop - 10000000

# cProfile.run('func_1(10000000)')
# 1    0.002    0.002    0.002    0.002 task_1.py:9(func_1) - 10000
# 1    0.016    0.016    0.016    0.016 task_1.py:9(func_1) - 100000
# 1    0.142    0.142    0.142    0.142 task_1.py:9(func_1) - 1000000
# 1    1.464    1.464    1.464    1.464 task_1.py:9(func_1) - 10000000

# вариант 2


def func_2(n):
    summa_ = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return summa_

# 100 loops, best of 5: 696 nsec per loop - 10000
# 100 loops, best of 5: 772 nsec per loop - 100000
# 100 loops, best of 5: 776 nsec per loop - 1000000
# 100 loops, best of 5: 781 nsec per loop - 10000000

# cProfile.run('func_2(10000000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:24(func_2) - 10000
# 1    0.000    0.000    0.000    0.000 task_1.py:24(func_2) - 100000
# 1    0.000    0.000    0.000    0.000 task_1.py:24(func_2) - 1000000
# 1    0.000    0.000    0.000    0.000 task_1.py:24(func_2) - 10000000


print(f"Сумма {qnt} элементов ряда (вариант 1): {func_1(qnt)}")
print(f"Сумма {qnt} элементов ряда (вариант 2): {func_2(qnt)}")

# ВЫВОД: варинат 2 с геоментрической прогрессией очевидно более привлекателен по скорости.
# Это особенно заметно на большом количестве элементов ряда.






