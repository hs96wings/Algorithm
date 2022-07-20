#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    int a, b, c;
    cin >> a >> b >> c;

    if (b >= c) {
        cout << -1 << '\n';
    } else {
        cout << a / (c - b) + 1 << '\n';
    }

    return 0;
}