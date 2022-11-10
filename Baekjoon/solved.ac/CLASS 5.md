### [2467번 용액](https://boj.kr/2467)

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.  
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고,  
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.  
이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때,  
이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
gap = arr[0] + arr[-1]

left = 0
right = n - 1
left_val = right_val = 0
while left < right:
    tmp = arr[left] + arr[right]

    if abs(tmp) <= abs(gap):
        gap = tmp
        left_val = arr[left]
        right_val = arr[right]
        if tmp == 0:
            break

    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
print(left_val, right_val)
```
