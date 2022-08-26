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