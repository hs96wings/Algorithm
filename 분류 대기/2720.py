# 2720번 세탁소 사장 동혁 (그리디 알고리즘)

import sys

n = int(sys.stdin.readline())
coins = [25, 10, 5, 1]

for _ in range(n):
    c = int(sys.stdin.readline())
    for coin in coins:
        cnt = 0
        cnt += c // coin
        c %= coin
        print(cnt, end=' ')
    print()