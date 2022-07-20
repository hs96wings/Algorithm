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
