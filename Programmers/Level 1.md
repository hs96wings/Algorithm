## Level 1

### [로또의 최고 순위와 최저 순위](https://school.programmers.co.kr/learn/courses/30/lessons/77484)

```python
def solution(lottos, win_nums):
    count_0 = lottos.count(0)
    lottos_set = set(lottos)
    win_set = set(win_nums)
    correct = len(lottos_set & win_set)
    answer = []

    tmp = correct + count_0
    grade = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    # 최고 순위는 일치한 개수에 지워진 숫자도 일치할 경우이므로
    # 로또와 숫자의 합집합 개수에 0의 갯수 포함
    answer.append(grade[tmp])
    # 최저 순위는 일치한 개수에 지워진 숫자 미포함이므로 일치한 개수만 구하기
    answer.append(grade[correct])

    return answer
```

---

### [신규 아이디 추천](https://school.programmers.co.kr/learn/courses/30/lessons/72410)

```python
import re

def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # 3단계
    new_id = re.sub(r'[.]{2,}', '.', new_id)
    # 4단계
    # Index Error이 나오므로 길이별 처리를 함
    if len(new_id) > 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        if new_id == '.':
            new_id = ''
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer
```

---

### [없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051)

```python
def solution(numbers):
    answer = 0
    data = [x for x in range(1, 10)]
    result = list(set(data) - set(numbers))
    for i in result:
        answer += i
    return answer
```

---

### [음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

```python
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer = answer + absolutes[i] if signs[i] else answer - absolutes[i]
    return answer
```

---

### [3진법 뒤집기](https://school.programmers.co.kr/learn/courses/30/lessons/68935)

```python
def solution(n):
    answer = ''

    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)

    answer = int(answer, 3)
    return answer
```

---

### [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644)

```python
from itertools import combinations

def solution(numbers):
    answer = []
    result = list(combinations(numbers, 2))

    for i in result:
        k, v = i
        answer.append(k + v)

    answer = list(set(answer))
    answer.sort()

    return answer
```

---

### [\[1차\] 비밀지도](https://school.programmers.co.kr/learn/courses/30/lessons/17681)

```python
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = arr1[i] | arr2[i]
        tmp = bin(tmp)[2:]
        if len(tmp) < n:
            tmp = '0' * (n - len(tmp)) + tmp
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer
```

---

### [나누어 떨어지는 숫자 배열](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

```python
def solution(arr, divisor):
    result = [x for x in arr if x % divisor == 0]
    result.sort()
    return result if len(result) > 0 else [-1]
```

---

### [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915)

```python
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
```

---

### [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

```python
def solution(s):
    s = s.lower()

    count_p = count_y = 0
    for i in range(len(s)):
        if s[i] == 'p':
            count_p += 1
        elif s[i] == 'y':
            count_y += 1

    if count_p == count_y:
        return True
    else:
        return False
```

---

### [문자열 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12917)

```python
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)
```

---

### [서울에서 김서방 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12919)

```python
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"
```

---

### [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12921)

```python
import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    memory = []
    data = [x for x in range(2, n + 1)]

    for i in data:
        if is_prime(i):
            memory.append(i)

    answer = len(memory)
    return answer
```

---

### [수박수박수박수박수박수?](https://school.programmers.co.kr/learn/courses/30/lessons/12922)

```python
def solution(n):
    answer = '수박' * (n // 2)
    if n % 2 == 1:
        answer += '수'
    return answer
```

---

### [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/12931)

```python
def solution(n):
    n = list(str(n))
    n = [int(x) for x in n]
    return sum(n)
```

---

### [자연수 뒤집어 배열로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

```python
def solution(n):
    answer = []
    n = list(str(n)[::-1])
    for i in n:
        answer.append(int(i))
    return answer
```

---

### [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

```python
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    answer = int(''.join(n))
    return answer
```

---

### [제일 작은 수 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12935)

```python
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr = [-1]
    return arr
```

---

### [짝수와 홀수](https://school.programmers.co.kr/learn/courses/30/lessons/12937)

```python
def solution(num):
    return "Odd" if num % 2 else "Even"
```

---

### [최대공약수와 최소공배수](https://school.programmers.co.kr/learn/courses/30/lessons/12940)

```python
import math

def solution(n, m):
    answer = []
    tmp = math.gcd(n, m)
    answer.append(tmp)
    answer.append(n * m // tmp)
    return answer
```

---

### [콜라츠 추측](https://school.programmers.co.kr/learn/courses/30/lessons/12943)

```python
def solution(num):
    answer = 0
    while True:
        if num == 1 or answer == 500:
            break
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        answer += 1
    return answer if answer < 500 else -1
```

---

### [평균 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/12944)

```python
def solution(arr):
    return sum(arr) / len(arr)
```

---

### [하샤드 수](https://school.programmers.co.kr/learn/courses/30/lessons/12947)

```python
def solution(x):
    total = sum([int(i) for i in str(x)])
    return True if x % total == 0 else False
```

---

### [핸드폰 번호 가리기](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

```python
def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]
```

---

### [x만큼 간격이 있는 n개의 숫자](https://school.programmers.co.kr/learn/courses/30/lessons/12954)

```python
def solution(x, n):
    answer = []
    answer.append(x)
    result = x
    for _ in range(n - 1):
        result += x
        answer.append(result)
    return answer
```

---

### [직사각형 별찍기](https://school.programmers.co.kr/learn/courses/30/lessons/12969)

```python
a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
```
