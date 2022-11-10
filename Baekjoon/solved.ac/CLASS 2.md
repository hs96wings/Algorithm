### [1259번 팰린드롬수](https://boj.kr/1259)

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

### [10845번 큐](https://boj.kr/10845)

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

### [15829번 Hashing](https://boj.kr/15829)

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

---

### [1018번 체스판 다시 칠하기](https://boj.kr/1018)

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.  
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.  
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.  
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.  
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.  
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서,  
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.  
당연히 8\*8 크기는 아무데서나 골라도 된다.  
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

```text
브루트포스는 처음 접해봐서 어떻게 풀어야할지 막막했다
```

```python
import sys
input = sys.stdin.readline

size = 8
str1 = 'WBWBWBWB'
str2 = 'BWBWBWBW'
pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
result = int(1e9)

for i in range(n - size + 1):
    for j in range(m - size + 1):
        cnt = 0
        for p in range(size):
            for q in range(size):
                if board[i+p][j+q] != pivot1[p][q]:
                    cnt += 1
        result = min(result, cnt)
        cnt = 0
        for p in range(size):
            for q in range(size):
                if board[i+p][j+q] != pivot2[p][q]:
                    cnt += 1
        result = min(result, cnt)
print(result)
```

---

### [18111번 마인크래프트](https://boj.kr/18111)

팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다.  
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.

목재를 충분히 모은 lvalue는 집을 짓기로 하였다.  
하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.

lvalue는 세로 N, 가로 M 크기의 집터를 골랐다.  
집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다.  
우리는 다음과 같은 두 종류의 작업을 할 수 있다.

좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.  
인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.  
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.  
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다.  
또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다.  
땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

```text
시간 초과로 인해 PyPy3로 제출함
```

```python
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)
pos = 0

# 0층부터 257층까지
for lv in range(257):
    lo, hi = 0, 0

    for i in range(n):
        for j in range(m):

            # 쌓인 블록이 층수보다 클 경우
            if graph[i][j] >= lv:
                hi += graph[i][j] - lv
            # 작을 경우
            else:
                lo += lv - graph[i][j]

    # 인벤토리가 음수가 되면 안 되므로 파낸 블록과 인벤토리의 합이 더 커야함
    if hi + b >= lo:
        # 최저 시간 비교
        if lo + (hi * 2) <= result:
            result = lo + (hi * 2)
            pos = lv

print(result, pos)
```

```text
0~256까지 탐색하지 말고 최저 높이와 최고 높이를 구해 범위를 특정할 수 있지만 0~256까지 탐색했을 땐 800ms, 범위 특정 시 816ms로 전부 탐색했을 때가 조금 더 빨랐다
```

```python
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
lo_block = min([min(x) for x in graph])
hi_block = max([max(x) for x in graph])
result = int(1e9)
pos = 0

# 최저 높이부터 최고 높이까지
for lv in range(lo_block, hi_block + 1):
    lo, hi = 0, 0

    for i in range(n):
        for j in range(m):

            # 쌓인 블록이 층수보다 클 경우
            if graph[i][j] >= lv:
                hi += graph[i][j] - lv
            # 작을 경우
            else:
                lo += lv - graph[i][j]

    # 인벤토리가 음수가 되면 안 되므로 파낸 블록과 인벤토리의 합이 더 커야함
    if hi + b >= lo:
        # 최저 시간 비교
        if lo + (hi * 2) <= result:
            result = lo + (hi * 2)
            pos = lv

print(result, pos)
```
