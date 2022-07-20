# 10988번 팰린드롬인지 확인하기

import sys

s = sys.stdin.readline().rstrip()
rs = s[::-1]

if s == rs:
    print(1)
else:
    print(0)