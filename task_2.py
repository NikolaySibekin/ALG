# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

import heapq
import collections


class Node(collections.namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):

        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(collections.namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(str_):
    h = []

    for ch, freq in collections.Counter(str_).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


my_str = input('Введите строку для кодирования:\n')
code_s = huffman_encode(my_str)
encoded = "".join(code_s[ch] for ch in my_str)
print(f'Число символов в строке: {len(code_s)}')

print('*' * 50)
print('Символ и соответствующий ему код в словаре')
for ch in sorted(code_s):
    print(f'{ch}: {code_s[ch]}')

print('*' * 50)
print(f'Закодированная строка:\n{encoded}')
print(f'Длина закодированной строки: {len(encoded)}')
