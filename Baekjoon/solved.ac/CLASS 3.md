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
