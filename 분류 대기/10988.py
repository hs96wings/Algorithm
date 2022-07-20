import sys

s = sys.stdin.readline().rstrip()
rs = s[::-1]

if s == rs:
    print(1)
else:
    print(0)