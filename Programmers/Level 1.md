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

---

### [성격 유형 검사하기](https://school.programmers.co.kr/learn/courses/30/lessons/118666)

```python
def solution(survey, choices):
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    order = ['RT', 'CF', 'JM', 'AN']
    answer = ''
    for i in range(len(survey)):
        if choices[i] >= 5:
            dic[survey[i][1]] += scores[choices[i]]
        else:
            dic[survey[i][0]] += scores[choices[i]]

    for i in range(4):
        if dic[order[i][0]] > dic[order[i][1]]:
            answer += order[i][0]
        elif dic[order[i][0]] == dic[order[i][1]]:
            if ord(order[i][0]) > ord(order[i][1]):
                answer += order[i][1]
            else:
                answer += order[i][0]
        else:
            answer += order[i][1]
    return answer
```

---

### [두 정수 사이의 합](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

```python
def solution(a, b):
    answer = 0
    for i in range(min(a, b), max(a, b) + 1):
        answer += i
    return answer
```

---

### [정수 제곱근 판별](https://school.programmers.co.kr/learn/courses/30/lessons/12934)

```python
def solution(n):
    answer = 0
    t = n ** 0.5

    if n // t == t:
        answer = (int(t) + 1) ** 2
    else:
        answer = -1
    return answer
```

---

### [가운데 글자 가져오기](https://school.programmers.co.kr/learn/courses/30/lessons/12903)

```python
def solution(s):
    return s[len(s) // 2] if len(s) % 2 == 1 else s[len(s) // 2 - 1: len(s) // 2 + 1]
```

---

### [문자열을 정수로 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/12925)

```python
def solution(s):
    return int(s)
```

---

### [내적](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

```python
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])
```

---

### [행렬의 덧셈](https://school.programmers.co.kr/learn/courses/30/lessons/12950)

```python
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1
```

---

### [시저 암호](https://school.programmers.co.kr/learn/courses/30/lessons/12926)

```python
def solution(s, n):
    answer = ''
    for i in range(len(s)):
        tmp = ord(s[i]) + n
        # 띄어쓰기
        if ord(s[i]) == 32:
            answer += ' '
        else:
            # 대문자일 경우
            if 65 <= ord(s[i]) <= 90:
                if tmp > 90:
                    tmp -= 26
            else:
                if tmp > 122:
                    tmp -= 26
            answer += chr(tmp)
    return answer
```

---

### [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

```python
def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = score2 = score3 = 0
    q_num = len(answers)

    if len(stu1) < q_num:
        stu1 = stu1 * (q_num // len(stu1) + 1)
    if len(stu2) < q_num:
        stu2 = stu2 * (q_num // len(stu2) + 1)
    if len(stu3) < q_num:
        stu3 = stu3 * (q_num // len(stu3) + 1)

    for i in range(q_num):
        if stu1[i] == answers[i]:
            score1 += 1
        if stu2[i] == answers[i]:
            score2 += 1
        if stu3[i] == answers[i]:
            score3 += 1

    hi_score = max(score1, score2, score3)
    if score1 == hi_score:
        answer.append(1)
    if score2 == hi_score:
        answer.append(2)
    if score3 == hi_score:
        answer.append(3)
    return answer
```

---

### [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301)

```python
from collections import deque

def solution(s):
    data = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = ''
    tmp = ''
    q = deque(list(s))

    while q:
        t = q.popleft()

        if t.isdigit():
            answer += t
        else:
            tmp += t
            if tmp in data:
                answer += data[tmp]
                tmp = ''
    return int(answer)
```
