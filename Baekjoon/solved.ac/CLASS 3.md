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
