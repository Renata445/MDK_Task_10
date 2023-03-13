# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

N = int(input())
a = {}
for i in range(N):
    b = input().split()
    cityes, country = b[1:], b[0]
    for city in cityes:
        a[city] = country
for i in range(int(input())):
    print(a[input()])

