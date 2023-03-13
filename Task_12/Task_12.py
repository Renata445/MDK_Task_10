# Даны два элемента в дереве. Определите, является ли один из них потомком другого.

# Во входных данных записано дерево в том же формате, что и в предыдущей задаче
# Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.

# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2,
# если второй является предком первого или 0, если ни один из них не является предком другого.

def a(m, om):
    if m == om:
        return True
    while m in p:
        m = p[m]
        if m == om:
            return True
    return False
    
p = dict()
N = int(input())
for i in range(N - 1):
    child, parent = input().split()
    p[child] = parent

for i in range(int(input())):
    first, second = input().split()
    if a(second, first):
        print(1, end=' ')
    elif a(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')