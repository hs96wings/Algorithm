### [2475번 검증수](https://boj.kr/2475)

검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.

예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면,  
각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.

첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

첫째 줄에 검증수를 출력한다.

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0, i, t;

    for (i = 0; i < 5; ++i) {
        cin >> t;
        sum += t * t;
    }

    cout << sum % 10;

    return 0;
}
```

```python
num_list = list(map(int, input().split()))
sum = 0

for num in num_list:
    sum += num ** 2

print(sum % 10)
```

---

### [2920번 음계](https://boj.kr/2920)

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.  
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

```cpp
#include <iostream>
using namespace std;

int main() {
    int i, n, op;
    int arr[8];

    for (i = 0; i < 8; ++i) {
        cin >> arr[i];
    }

    for (i = 0; i < 7; ++i) {
        if (arr[i + 1] - arr[i] == 1) {
            op = 1;
        } else if (arr[i + 1] - arr[i] == -1) {
            op = -1;
        } else {
            op = 0;
        }

        if (op == 0) {
            break;
        }
    }

    switch (op) {
        case 1:
            cout << "ascending";
            break;
        case -1:
            cout << "descending";
            break;
        default:
            cout << "mixed";
    }

    return 0;
}
```

```python
ascend = [1, 2, 3, 4, 5, 6, 7, 8]
desend = [8, 7, 6, 5, 4, 3, 2, 1]

num_list = list(map(int, input().split()))

if num_list == ascend:
    print('ascending')
elif num_list == desend:
    print('descending')
else:
    print('mixed')
```

```python
# 사전에 리스트를 적지 않았을 경우
num_list = list(map(int, input().split()))
op = 0

for i in range(0, 7):
    if num_list[i + 1] - num_list[i] == 1:
        op = 1
    elif num_list[i + 1] - num_list[i] == -1:
        op = -1
    else:
        op = 0
        break

if op == 1:
    print('ascending')
elif op == -1:
    print('descending')
else:
    print('mixed')

```
