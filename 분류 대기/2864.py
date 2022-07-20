# 2864번 5와 6의 차이 (그리디 알고리즘)

import sys

a, b = map(str, sys.stdin.readline().rstrip().split())
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)