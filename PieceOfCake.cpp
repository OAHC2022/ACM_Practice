using namespace std;
#include <iostream>


int main() {

    int N, H, V;
    cin >> N >> H >> V;
    int side1 = max(H, N-H);
    int side2 = max(V, N-V);
    cout << (4 * side1 * side2);

    return 0;
}