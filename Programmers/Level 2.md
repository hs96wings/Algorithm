## Level 2

### [문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057)

```python
def solution(s):
    answer = len(s)
    for step in range(1, answer // 2 + 1):
        tmp = ''
        prev = s[0:step]
        cnt = 1
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                if cnt >= 2:
                    tmp += str(cnt) + prev
                else:
                    tmp += prev
                prev = s[i:i+step]
                cnt = 1
        if cnt >= 2:
            tmp += str(cnt) + prev
        else:
            tmp += prev
        answer = min(answer, len(tmp))
    return answer
```

---

### [JadenCase 문자열 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951)

```text
첫 번째 문자열만 처리해주고 나머지 문자를 처리해주었다
같이 처리해줄 경우 s[i - 1]에서 Index Error가 생기기 때문이다
공백 문자가 연속해서 나올 수 있으므로 이전 문자가 공백이고 지금 문자열이 알파벳인 경우에만 대문자로 바꾸어주고 나머지는 소문자로 바꾼다
```

```python
def solution(s):
    answer = ''

    # 첫 번째 문자 처리
    if s[0] != ' ' and not s[0].isdigit():
        answer += s[0].upper()
    else:
        answer += s[0]

    # 나머지 문자 처리
    for i in range(1, len(s)):
        # 이전 문자가 공백이고 지금 문자열이 알파벳이라면
        if s[i - 1] == ' ' and not s[i].isdigit():
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer
```

---

### [최댓값과 최솟값](https://school.programmers.co.kr/learn/courses/30/lessons/12939)

```python
def solution(s):
    answer = ''
    tmp = list(map(int, s.split()))
    return f'{min(tmp)} {max(tmp)}'
```
