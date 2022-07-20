### [10989번 수 정렬하기 3](https://www.acmicpc.net/problem/10989)

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

```text
list 전부 넣고 sort() 쓰니 메모리 초과 오류 나와서
dict 사용하여 빈도수 체크하고 빈도만큼 출력하게 함
```

```python
import sys

n = int(sys.stdin.readline())
data = dict()

for i in range(n):
    t = int(sys.stdin.readline())
    if t in data:
        data[t] += 1
    else:
        data[t] = 1

data = sorted(data.items())

for k, v in data:
    for _ in range(v):
        print(k)
```

---

### [2751번 수 정렬하기 2](https://www.acmicpc.net/problem/2751)

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.  
수는 중복되지 않는다.

```text
10989번과 같은 코드로 풀리긴 했는데 '수는 중복되지 않는다'를 늦게 봐서 그냥 리스트에 넣고 정렬함
10989번이 더 어려운 거 같음
```

```python
import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

for i in range(n):
    print(data[i])
```

---

### [10845번 큐](https://www.acmicpc.net/problem/10845)

push X: 정수 X를 큐에 넣는 연산이다.  
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.  
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
size: 큐에 들어있는 정수의 개수를 출력한다.  
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.  
front: 큐의 가장 앞에 있는 정수를 출력한다.  
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
back: 큐의 가장 뒤에 있는 정수를 출력한다.  
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    cin.tie(NULL);
    int n, t;
    queue<int> q;
    string s;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> s;

        if (s == "push") {
            cin >> t;
            q.push(t);
        } else if (s == "pop") {
            if (!q.empty()) {
                cout << q.front() << '\n';
                q.pop();
            } else {
                cout << -1 << '\n';
            }
        } else if (s == "size") {
            cout << q.size() << '\n';
        } else if (s == "empty") {
            if (!q.empty()) {
                cout << 0 << '\n';
            } else {
                cout << 1 << '\n';
            }
        } else if (s == "front") {
            if (!q.empty()) {
                cout << q.front() << '\n';
            } else {
                cout << -1 << '\n';
            }
        } else if (s == "back") {
            if (!q.empty()) {
                cout << q.back() << '\n';
            } else {
                cout << -1 << '\n';
            }
        }
    }

    return 0;
}
```

```python
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        queue.append(op[1])
    elif op[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif op[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
```

---
