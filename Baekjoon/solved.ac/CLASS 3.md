### [1676번 팩토리얼 0의 개수](https://www.acmicpc.net/problem/1676)

N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

```text
Factorial 재귀 함수로 풀다가 런타임 에러 (RecursionError)로 math.factorial 사용
```

```python
import sys
import math
n = int(sys.stdin.readline())

fac = list(str(math.factorial(n)))
fac.reverse()
cnt = 0

for f in fac:
    if f == '0':
        cnt += 1
    else:
        if cnt != 0:
            break

print(cnt)
```

---

### [11723번 집합](https://www.acmicpc.net/problem/11723)

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.  
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.  
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)  
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)  
all: S를 {1, 2, ..., 20} 으로 바꾼다.  
empty: S를 공집합으로 바꾼다.

```python
import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    data = sys.stdin.readline().rstrip().split()

    if len(data) == 1:
        if data[0] == 'all':
            s = set([x for x in range(1, 21)])
        else:
            s = set()
    else:
        op, num = data[0], data[1]
        num = int(num)

        if op == 'add':
            s.add(num)
        elif op == 'remove':
            s.discard(num)
        elif op == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)
```

---

### [1620번 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)

첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.  
N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와.  
포켓몬의 이름은 모두 영어로만 이루어져있고, 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야.  
그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와.  
문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해.

```python
import sys
n, m = map(int, sys.stdin.readline().split())

data = {}

for i in range(1, n + 1):
    t = sys.stdin.readline().rstrip()
    data[i] = t
    data[t] = i

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(data[int(q)])
    else:
        print(data[q])

```

---

### [1764번 듣보잡](https://www.acmicpc.net/problem/1764)

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.  
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,  
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.  
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.  
N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

```text
교집합
```

```python
import sys
n, m = map(int, sys.stdin.readline().split())

s1 = set()
s2 = set()

for _ in range(n):
    s1.add(sys.stdin.readline().rstrip())
for _ in range(m):
    s2.add(sys.stdin.readline().rstrip())

s3 = s1 & s2
s3 = sorted(s3)
print(len(s3))
for s in s3:
    print(s)
```

---

### [11047 동전 0](https://www.acmicpc.net/problem/11047)

```text
그리디 알고리즘 기초 문제
```

```cpp
#include <iostream>

using namespace std;

int main() {
    int n, k, count = 0;
    int coins[10] = {};

    cin >> n >> k;

    for (int i = n - 1; i >= 0; --i) {
        cin >> coins[i];
    }

    for (int i = 0; i < n; ++i) {
        count += k / coins[i];
        k %= coins[i];
    }

    cout << count << endl;
    return 0;
}
```

```python
n, k = map(int, input().split())
count = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

coins = sorted(coins, reverse=True)

for coin in coins:
    count += k // coin
    k %= coin

print(count)
```
