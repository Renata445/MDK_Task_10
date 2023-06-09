# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.

# Вам дано генеалогическое древо, определите высоту всех его элементов.

# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка,
# задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

# Программа должна вывести список всех элементов древа в лексикографическом порядке.
# После вывода имени каждого элемента необходимо вывести его высоту.

# Примечание

# Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2)
# (не считая сложности обращения к элементам словаря).

def h(m):
    if m not in p:
        return 0
    else:
        return 1 + h(p[m])

p = {}
N = int(input())
for i in range(N - 1):
    child, parent = input().split()
    p[child] = parent

hs = {}
for m in set(p.keys()).union(set(p.values())):
    hs[m] = h(m)

for key, value in sorted(hs.items()):
    print(key, value)
