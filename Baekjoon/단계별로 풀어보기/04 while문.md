## 04 while문

### [10952 A+B - 5](https://www.acmicpc.net/problem/10952)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.  
입력의 마지막에는 0 두 개가 들어온다.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int a, b;
    while (true) {
        cin >> a >> b;
        if (a == 0 && b == 0)
            break;
        cout << a + b << "\n";
    }

    return 0;
}
```

---

### [10951번 A+B - 4](https://www.acmicpc.net/problem/10951)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int a, b;
    while (cin >> a >> b) {
        cout << a + b << "\n";
    }

    return 0;
}
```

---

### [1110번 더하기 사이클](https://www.acmicpc.net/problem/1110)

0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.  
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.  
그 다음, 주어진 수의 가장 오른쪽 자리 수와  
앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

26부터 시작한다. 2+6 = 8이다.  
새로운 수는 68이다. 6+8 = 14이다.  
새로운 수는 84이다. 8+4 = 12이다.  
새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int n, o, s = 0;
    cin >> n;
    o = n;
    while (true) {
        n = (n % 10) * 10 + ((n / 10) + (n % 10)) % 10;
        s++;

        if (n == o)
            break;
    }
    cout << s;
    return 0;
}
```
