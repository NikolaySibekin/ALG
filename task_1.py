# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

Firm = namedtuple('Firm', ['name', 'quarters', 'profit'])
companies = set()

n = int(input("Введите количество предприятий: "))
total_profit = 0

for i in range(1, n + 1):
    name = input(str(i) + "-я фирма: ")
    profit = 0
    quarters = []

    for j in range(4):
        quarters.append(int(input(f"Прибыль за {j + 1} квартал: ")))
        profit += quarters[j]

    firm = Firm(name=name, quarters=tuple(quarters), profit=profit)
    companies.add(firm)
    total_profit += profit

average_profit = total_profit / n

print(f"Средняя прибыль за год для всех предприятий:{average_profit}")

print("\nФирмы с прибылью выше среднего:")

for firm in companies:
    if firm.profit > average_profit:
        print(f"Фирма {firm.name}, прибыль {firm.profit}")

print("\nФирмы с прибылью ниже среднего:")

for firm in companies:
    if firm.profit < average_profit:
        print(f"Фирма {firm.name}, прибыль {firm.profit}")
