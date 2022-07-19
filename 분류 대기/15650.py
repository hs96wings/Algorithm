# 15650번 N과 M (2)

from itertools import combinations

n, m = map(int, input().split())

data = [x for x in range(1, n + 1)]

result = list(combinations(data, m))
for res in result:
    for i in res:
        print(i, end = ' ')
    print()