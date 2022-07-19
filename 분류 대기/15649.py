# 15649번 N과 M (1)

from itertools import permutations

n, m = map(int, input().split())

data = [x for x in range(1, n + 1)]

result = list(permutations(data, m))
for res in result:
    for i in res:
        print(i, end = ' ')
    print()