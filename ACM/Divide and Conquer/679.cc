#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

int P_helper(ll D, ll I, ll sum) {
	if (I == 1) {
		return sum;
	}
	if (I % 2 == 0) {
		return P_helper(D, I-1, sum+pow(2,D-2));
	} else {
		return P_helper(D-1,(I+1)/2, sum);
	}
}

// 20 >= D >= 2
int P(ll D, ll I) {
	return P_helper(D, I, 0) + pow(2,D-1);
}

int main() {
	ll N, D, I;
	cin >> N; // number of test cases
	for (ll cs = 0; cin >> D >> I; ++cs) {
		cout << P(D, I) << endl;
	}
	return 0;
}