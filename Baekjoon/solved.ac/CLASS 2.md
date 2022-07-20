### [1085번 직사각형에서 탈출](https://www.acmicpc.net/problem/1085)

한수는 지금 (x, y)에 있다.  
직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.  
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

```text
(w - x), (h - y), x, y 중 최소값이 거리의 최소값
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    if (w - x <= h - y && w - x <= x && w - x <= y) {
        cout << w - x;
    } else if (h - y <= w - x && h - y <= x && h - y <= y) {
        cout << h - y;
    } else if (x <= w - x && x <= h - y && x <= y) {
        cout << x;
    } else {
        cout << y;
    }

    return 0;
}
```

```python
x, y, w, h = map(int, input().split())

print(min(w-x, h-y, x, y))
```

---

### [4135번 직각삼각형](https://www.acmicpc.net/problem/4153)

주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

```text
피타고라스의 정리 빗변^2 = 밑변^2 + 높이^2
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    while (true) {
        cin >> a >> b >> c;
        if (a + b + c == 0) {
            break;
        }
        if (a >= b && a >= c) {
            if (a * a == b * b + c * c) {
                cout << "right\n";
            } else {
                cout << "wrong\n";
            }
        } else if (b >= a && b >= c) {
            if (b * b == a * a + c * c) {
                cout << "right\n";
            } else {
                cout << "wrong\n";
            }
        } else {
            if (c * c == a * a + b * b) {
                cout << "right\n";
            } else {
                cout << "wrong\n";
            }
        }
    }

    return 0;
}
```

```python
while True:
    sides = list(map(int, input().split()))
    if sum(sides) == 0:
        break
    sides.sort()
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print('right')
    else:
        print('wrong')
```

---

### [2798번 블랙잭](https://www.acmicpc.net/problem/2798)

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

```python
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards_comb = list(combinations(cards, 3))
cards_sum = []
for comb in cards_comb:
    t = sum(comb)
    if t <= m:
        cards_sum.append(t)
print(max(cards_sum))
```

---

### [2609번 최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609)

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

```python
import math

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = a * b // gcd

print(gcd)
print(lcm)
```

---

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

### [2164번 카드2](https://www.acmicpc.net/problem/2164)

우선, 제일 위에 있는 카드를 바닥에 버린다.  
그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.  
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    cin.tie(NULL);
    int n, t;
    queue<int> q;

    cin >> n;
    for (int i = 1; i <= n; ++i) {
        q.push(i);
    }

    while (q.size() > 1) {
        q.pop();
        t = q.front();
        q.pop();
        q.push(t);
    }

    cout << q.front() << '\n';

    return 0;
}
```

```python
import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([x for x in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    k = queue.popleft()
    queue.append(k)

print(queue.popleft())
```

---

### [10773번 제로](https://www.acmicpc.net/problem/10773)

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.  
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    cin.tie(NULL);
    int n, t;
    stack<int> s;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> t;
        if (t == 0) {
            s.pop();
        } else {
            s.push(t);
        }
    }

    int result = 0;

    while (!s.empty()) {
        result += s.top();
        s.pop();
    }

    cout << result << '\n';

    return 0;
}
```

```python
import sys
k = int(sys.stdin.readline())

stack = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
```

---

### [10828번 스택](https://www.acmicpc.net/problem/10828)

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.  
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.  
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
size: 스택에 들어있는 정수의 개수를 출력한다.  
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.  
top: 스택의 가장 위에 있는 정수를 출력한다.  
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    cin.tie(NULL);
    int n, t;
    stack<int> s;
    string str;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> str;

        if (str == "push") {
            cin >> t;
            s.push(t);
        } else if (str == "pop") {
            if (!s.empty()) {
                cout << s.top() << '\n';
                s.pop();
            } else {
                cout << -1 << '\n';
            }
        } else if (str == "size") {
            cout << s.size() << '\n';
        } else if (str == "empty") {
            if (!s.empty()) {
                cout << 0 << '\n';
            } else {
                cout << 1 << '\n';
            }
        } else if (str == "top") {
            if (!s.empty()) {
                cout << s.top() << '\n';
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
n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
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

### [10866번 덱](https://www.acmicpc.net/problem/10866)

push_front X: 정수 X를 덱의 앞에 넣는다.  
push_back X: 정수 X를 덱의 뒤에 넣는다.  
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.  
만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.  
만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
size: 덱에 들어있는 정수의 개수를 출력한다.  
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.  
front: 덱의 가장 앞에 있는 정수를 출력한다.  
만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.  
back: 덱의 가장 뒤에 있는 정수를 출력한다.  
만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

```cpp
#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
    cin.tie(NULL);
    int n, t;
    deque<int> d;
    string s;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> s;

        if (s == "push_front") {
            cin >> t;
            d.push_front(t);
        } else if (s == "push_back") {
            cin >> t;
            d.push_back(t);
        } else if (s == "pop_front") {
            if (!d.empty()) {
                cout << d.front() << '\n';
                d.pop_front();
            } else {
                cout << -1 << '\n';
            }
        } else if (s == "pop_back") {
            if (!d.empty()) {
                cout << d.back() << '\n';
                d.pop_back();
            } else {
                cout << -1 << '\n';
            }
        } else if (s == "size") {
            cout << d.size() << '\n';
        } else if (s == "empty") {
            if (!d.empty()) {
                cout << 0 << '\n';
            } else {
                cout << 1 << '\n';
            }
        } else if (s == "front") {
            if (!d.empty()) {
                cout << d.front() << '\n';
            } else {
                cout << -1 << '\n';
            }
        } else if (s == "back") {
            if (!d.empty()) {
                cout << d.back() << '\n';
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

    if op[0] == 'push_front':
        queue.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        queue.append(int(op[1]))
    elif op[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif op[0] == 'pop_back':
        if (len(queue)) == 0:
            print(-1)
        else:
            print(queue.pop())
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
