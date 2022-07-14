## 03 for문

### [2739번 구구단](https://www.acmicpc.net/problem/2739)

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.  
출력 형식에 맞춰서 출력하면 된다.

```python
n = int(input())

for i in range(1, 10):
    print(n, '*', i, '=', n * i)
```

---

### [10950번 A+B - 3](https://www.acmicpc.net/problem/10950)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
n = int(input())

for i in range(0, n):
    a, b = map(int, input().split())
    print(a + b)
```

---

### [8393번 합](https://www.acmicpc.net/problem/8393)

n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

```python
n = int(input())
s = 0

for i in range(1, n+1):
    s += i
print(s)

```

```python
# 반복문 없이
n = int(input())
print(n * (n + 1) // 2)
```

---

### [15552번 빠른 A+B](https://www.acmicpc.net/problem/15552)

for문 문제를 풀기 전에 주의해야 할 점이 있다.  
입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.  
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.  
다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

```python
import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

```

---

### [2741번 N 찍기](https://www.acmicpc.net/problem/2741)

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
n = int(input())

for i in range(1, n+1):
    print(i)
```

---

### [2742번 기찍 N](https://www.acmicpc.net/problem/2742)

자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
n = int(input())

for i in range(0, n):
    print(n - i)
```

---

### [11021번 A+B - 7](https://www.acmicpc.net/problem/11021)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.  
테스트 케이스 번호는 1부터 시작한다.

```python
n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i, a+b))
```

---

### [11022 A+B - 8](https://www.acmicpc.net/problem/11022)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.  
x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

```python
n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i, a, b, a+b))
```

---

### [2438번 별 찍기 - 1](https://www.acmicpc.net/problem/2438)

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

```python
n = int(input())
for i in range(1, n+1):
    print('*' * i)
```

---

### [2439번 별 찍기 - 2](https://www.acmicpc.net/problem/2439)

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제  
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

```python
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    print('*' * i)
```

---

### [10871번 X보다 작은 수](https://www.acmicpc.net/problem/10871)

정수 N개로 이루어진 수열 A와 정수 X가 주어진다.  
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

```python

```
