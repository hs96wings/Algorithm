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

### [15829번 Hashing](https://www.acmicpc.net/problem/15829)

편의상 입력으로 들어오는 문자열에는 영문 소문자(a, b, ..., z)로만 구성되어있다고 가정하자.  
영어에는 총 26개의 알파벳이 존재하므로 a에는 1, b에는 2, c에는 3, ..., z에는 26으로 고유한 번호를 부여할 수 있다.  
결과적으로 우리는 하나의 문자열을 수열로 변환할 수 있다.  
예를 들어서 문자열 "abba"은 수열 1, 2, 2, 1로 나타낼 수 있다.

값을 계산하기 위해서 우리는 문자열 혹은 수열을 하나의 정수로 치환하려고 한다.  
간단하게는 수열의 값을 모두 더할 수도 있다.  
해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으니까 적당히 큰 수 M으로 나눠주자.

어떻게 하면 순서가 달라졌을때 출력값도 달라지게 할 수 있을까?  
머리를 굴리면 수열의 각 항마다 고유한 계수를 부여하면 된다는 아이디어를 생각해볼 수 있다.  
가장 대표적인 방법은 항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더하는 것이 있다.

보통 r과 M은 서로소인 숫자로 정하는 것이 일반적이다.  
우리가 직접 정하라고 하면 힘들테니까 r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891(놀랍게도 소수이다!!)로 하자.

```python
n = int(input())
s = input()

r = 31
m = 1234567891
result = 0
for i in range(n):
    tmp = ord(s[i]) - 96
    result += tmp * (r ** i)

print(result % m)
```
