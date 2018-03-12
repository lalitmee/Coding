#include <iostream>
#include <vector>
 
using namespace std;
 
unsigned long long f(unsigned long long val);
 
int main() {
    int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        unsigned long long a, n; cin >> a >> n;
        int period = 0, offset = 0;
        int fa = (int) f(a);
        vector<int> map = vector<int>(10);
        for (int j = 0; j < 10; ++j) {
            map[j] = (int) f(j * a);
        }
        if (n > 100) {
            vector<int> visited = vector<int>(10, -1);
            for (int j = 1; true; j++) {
                if (visited[fa] >= 0) {
                    offset = visited[fa] - 1;
                    period = j - visited[fa];
                    break;
                }
                visited[fa] = j;
                fa = map[fa];
            }
            if (n > offset) {
                n = ((n - offset) % period) + offset;
            }
            if (n == offset) n = (unsigned) period + offset;
        }
        fa = (int) f(a);
        for (int k = 0; (k + 1) < n; ++k) {
            fa = map[fa];
        }
        cout << fa << endl;
    }
    return 0;
}
 
unsigned long long f(unsigned long long val) {
    unsigned long long ans = 0;
    for (; val > 0; val /= 10) {
        ans += val % 10;
    }
    if (ans < 10) return ans;
    else return f(ans);
}
