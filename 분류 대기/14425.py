# 14425번 문자열 집합

import sys
n, m = map(int, sys.stdin.readline().split())

data = list()
for _ in range(n):
    data.append(sys.stdin.readline().rstrip())

cnt = 0

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    if s in data:
        cnt += 1

print(cnt)