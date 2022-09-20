### [17219번 비밀번호 찾기](https://www.acmicpc.net/problem/17219)

첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과  
비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.

두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다.  
사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있고, 중복되지 않는다.  
비밀번호는 알파벳 대문자로만 이루어져 있다. 모두 길이는 최대 20자이다.

N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다.  
이때, 반드시 이미 저장된 사이트 주소가 입력된다.

첫 번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 각 줄에 하나씩 출력한다.

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

data = dict()

for i in range(n):
    url, passwd = input().rstrip().split()
    data[url] = passwd

for i in range(m):
    str = input().rstrip()
    print(data[str])
```

---

### [9095번 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.  
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

```python
case = int(input())
dp = [0, 1, 2, 4]

for i in range(4, 11):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for _ in range(case):
    n = int(input())
    print(dp[n])
```

---

### [11726번 2xn 타일링](https://www.acmicpc.net/problem/11726)

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

```python
n = int(input())
dp = [0, 1, 2]

for i in range(3, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])

print(dp[n] % 10007)
```

---

### [11727번 2xn 타일링 2](https://www.acmicpc.net/problem/11727)

2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

```python
n = int(input())
dp = [0, 1, 3]

for i in range(3, n + 1):
    dp.append(dp[i - 1] + 2 * dp[i - 2])

print(dp[n] % 10007)
```

---

### [11724번 연결 요소의 개수](https://www.acmicpc.net/problem/11724)

방향 없는 그래프가 주어졌을 때,  
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

```text
그래프의 개수 구하기 문제
```

```python
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        # 단일 노드일 경우
        if not graph[i]:
            cnt += 1
            visited[i] = True
        # 연결된 노드일 경우
        else:
            bfs(i)
            cnt += 1

print(cnt)
```
