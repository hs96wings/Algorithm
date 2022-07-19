# 15650번 N과 M (3)

from itertools import product

n, m = map(int, input().split())

data = [x for x in range(1, n + 1)]

result = list(product(data, repeat=m))
for res in result:
    for i in res:
        print(i, end = ' ')
    print()