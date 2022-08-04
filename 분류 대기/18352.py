# 18352번 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = deque([x])
while q:
    v = q.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)

cnt = 0
for i in range(1, n + 1):
    if distance[i] == k:
        cnt += 1
        print(i)

if cnt == 0:
    print(-1)