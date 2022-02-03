## 03 for문

### [2739번 구구단](https://www.acmicpc.net/problem/2739)

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.  
출력 형식에 맞춰서 출력하면 된다.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= 9; i++)
        cout << n << " * " << i << " = " << (n * i) << endl;
    return 0;
}
```

---

### [10950번 A+B - 3](https://www.acmicpc.net/problem/10950)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a >> b;
        cout << a + b << endl;
    }
    return 0;
}
```

---

### [8393번 합](https://www.acmicpc.net/problem/8393)

n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n, s = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
        s += i;
    cout << s;
    return 0;
}
```

```cpp
// 반복문 없이
#include <iostream>

using namespace std;

int main() {
    int n, s = 0;
    cin >> n;
    cout << n * (n + 1) / 2 << endl;
    return 0;
}
```

---

### [15552번 빠른 A+B](https://www.acmicpc.net/problem/15552)

for문 문제를 풀기 전에 주의해야 할 점이 있다.  
입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면,  
cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고,  
endl 대신 개행문자(\n)를 쓰자.  
단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등  
C의 입출력 방식을 사용하면 안 된다.

첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.  
다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int n, i, a, b;
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> a >> b;
        cout << a + b << "\n";
    }

    return 0;
}
```

---

### [2741번 N 찍기](https://www.acmicpc.net/problem/2741)

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cout << i << "\n";

    return 0;
}
```

---

### [2742번 기찍 N](https://www.acmicpc.net/problem/2742)

자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = n; i >= 1; i--)
        cout << i << "\n";

    return 0;
}
```

---

### [11021번 A+B - 7](https://www.acmicpc.net/problem/11021)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.  
테스트 케이스 번호는 1부터 시작한다.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int n, i, a, b;
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> a >> b;
        cout << "Case #" << i << ": " << (a + b) << "\n";
    }

    return 0;
}
```

---

### [11022 A+B - 8](https://www.acmicpc.net/problem/11022)

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.  
x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int n, i, a, b;
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> a >> b;
        cout << "Case #" << i << ": " << a << " + " << b << " = " << (a + b) << "\n";
    }

    return 0;
}
```

---

### [2438번 별 찍기 - 1](https://www.acmicpc.net/problem/2438)

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

```cpp
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
```

---

### [2439번 별 찍기 - 2](https://www.acmicpc.net/problem/2439)

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제  
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    int n, i, j;
    cin >> n;
    for (i = 1; i <= n; i++) {
        for (j = n - i; j >= 1; j--) {
            cout << " ";
        }
        for (j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
```

---

### [10871번 X보다 작은 수](https://www.acmicpc.net/problem/10871)

정수 N개로 이루어진 수열 A와 정수 X가 주어진다.  
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int n, x, t;
    cin >> n >> x;
    for (int i = 1; i <= n; i++) {
        cin >> t;
        if (t < x)
            cout << t << " ";
    }

    return 0;
}
```
