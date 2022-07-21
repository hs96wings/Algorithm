### [1259번 팰린드롬수](https://www.acmicpc.net/problem/1259)

어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다.  
'radar', 'sees'는 팰린드롬이다.

수도 팰린드롬으로 취급할 수 있다.  
수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다.  
121, 12421 등은 팰린드롬수다.  
123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다.

또한 10도 팰린드롬수가 아닌데,  
앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만,  
특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.

```python
import sys

input = sys.stdin.readline

while True:
    str = input().rstrip()
    if str == '0':
        break

    if str == str[::-1]:
        print('yes')
    else:
        print('no')
```

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

### [1181번 단어 정렬](https://www.acmicpc.net/problem/1181)

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터  
길이가 같으면 사전 순으로

조건에 따라 정렬하여 단어들을 출력한다.  
단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

```python
import sys

input = sys.stdin.readline

n = int(input().rstrip())
data = []
for _ in range(n):
    data.append(input().rstrip())

data = set(data)
data = sorted(data)
data = sorted(data, key=lambda i: len(i))

for i in data:
    print(i)
```

---

### [1436번 영화감독 숌](https://www.acmicpc.net/problem/1436)

숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.  
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오.
숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

```python
import sys

input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
dooms = 666

while True:
    if '666' in str(dooms):
        cnt += 1

    if cnt == n:
        print(dooms)
        break

    dooms += 1
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

### [10814번 나이순 정렬](https://www.acmicpc.net/problem/10814)

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.  
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

```python
import sys

def sort_order(x):
    return x[2]

def sort_age(x):
    return x[0]

input = sys.stdin.readline

n = int(input().rstrip())
data = []

for i in range(n):
    str = input().rstrip().split()
    age, name = int(str[0]), str[1]
    data.append((age, name, i))

data = sorted(data, key=sort_order)
data = sorted(data, key=sort_age)

for i in data:
    print(i[0], i[1])
```

---

### [11650 좌표 정렬하기](https://www.acmicpc.net/problem/11650)

2차원 평면 위의 점 N개가 주어진다.  
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

```python
n = int(input())

graph = []
for _ in range(n):
    x, y = map(int, input().split())
    graph.append([x, y])

graph = sorted(graph, key=lambda x: x[1])
graph = sorted(graph, key=lambda x: x[0])

for x, y in graph:
    print(x, y)
```

---

### [11651 좌표 정렬하기 2](https://www.acmicpc.net/problem/11651)

2차원 평면 위의 점 N개가 주어진다.  
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

```text
11650 문제와 비교해서 정렬 순서만 바꿔주면 된다
11650번 문제 80%에서 엄청 오래 걸리길래 입력시간이라도 줄여보고자
sys.stdin.readline() 사용했다
```

```python
import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph.append([x, y])

graph = sorted(graph, key=lambda x: x[0])
graph = sorted(graph, key=lambda x: x[1])

for x, y in graph:
    print(x, y)
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
