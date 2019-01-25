# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

# 1 вариант:
num1 = input("Введите первое шестнадцатеричное число: ")
x = int(num1, 16)

num2 = input("Введите второе шестнадцатеричное число: ")
y = int(num2, 16)

z = x + y
k = x * y

print("Результат сложения: {0:02x}".format(z))
print("Результат умножения: {0:02x}".format(k))

print('*' * 50)
# 2 вариант:
BIN_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
           'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
HEX_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def conversion(hex_num):
    deque_num = deque(hex_num.upper())
    return deque_num


def sum_hex(num_first, num_second):
    num_first = num_first.copy()
    num_second = num_second.copy()

    if len(num_second) > len(num_first):
        num_first, num_second = num_second, num_first

    num_second.extendleft('0' * (len(num_first) - len(num_second)))

    result = deque()
    overflow = 0

    for i in range(len(num_first) - 1, -1, -1):
        first_num = BIN_NUM[num_first[i]]
        second_num = BIN_NUM[num_second[i]]
        result_num = first_num + second_num + overflow

        if result_num >= 16:
            overflow = 1
            result_num -= 16
        else:
            overflow = 0
        result.appendleft(HEX_NUM[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(num_first, num_second):
    num_first = num_first.copy()
    num_second = num_second.copy()

    if len(num_second) > len(num_first):
        num_first, num_second = num_second, num_first

    num_second.extendleft('0' * (len(num_first) - len(num_second)))

    result = deque('0')

    for i in range(len(num_first) - 1, -1, -1):
        second_num = BIN_NUM[num_second[i]]

        spam = deque('0')

        for _ in range(second_num):
            spam = sum_hex(spam, num_first)

        spam.extend('0' * (len(num_first) - i - 1))
        result = sum_hex(result, spam)

    return result


num3 = input("Введите первое шестнадцатеричное число: ")
num4 = input("Введите второе шестнадцатеричное число: ")

num3 = conversion(num3)
num4 = conversion(num4)

print(f"Результат сложения: {list(sum_hex(num3, num4))}")
print(f"Результат умножения: {list(mult_hex(num3, num4))}")
