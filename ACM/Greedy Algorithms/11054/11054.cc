#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;

ll n;
vi a(100000);

int main() {
	// Unit tests:

	// ifstream in("in.txt");
	// streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	// cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	while (cin>>n) {
		if (n==0) return 0;

		for (ll i=0; i<n; ++i) {
			cin>>a[i];
		}

		ll work = 0;
		for (ll i=0; i<n; i++) {
			if (a[i] != 0) {
				a[i+1] += a[i];
				work += abs(a[i]);
			}
		}

		cout << work << endl;
	}
	return 0;
}