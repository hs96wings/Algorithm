# 14659번 한조서열정리하고옴ㅋㅋ (그리디 알고리즘)
# 더 큰 수를 만나기 전까지 카운트 세기
# 마지막에 cnt.append(c) 한 이유는 처음이 가장 클 경우 cnt에 저장이 되지 않아 오류가 남
import sys

n = int(sys.stdin.readline())
archer = list(map(int, sys.stdin.readline().split()))
cnt = []
a = archer[0]
c = 0
for i in range(1, n):
    if a > archer[i]:
        c += 1
    else:
        cnt.append(c)
        c = 0
        a = archer[i]
cnt.append(c)
print(max(cnt))