// 11047번 동전 0

#include <iostream>

using namespace std;

int main() {
    int n, k, count = 0;
    int coins[10] = {};

    cin >> n >> k;

    for (int i = n - 1; i >= 0; --i) {
        cin >> coins[i];
    }

    for (int i = 0; i < n; ++i) {
        count += k / coins[i];
        k %= coins[i];
    }

    cout << count << endl;
    return 0;
}