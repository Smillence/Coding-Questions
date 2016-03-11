#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

typedef long long ll;
typedef map<ll, ll> dict;

ll N;
dict plane;

bool cover(ll L) {
	if (L==1) return true;

	for (dict::iterator it = plane.begin(); it != plane.end(); it++ ) {
		ll x=it->first, y=it->second;
		for (ll key=x-L+1; key<x+L; ++key) {
			if (key==x) continue;
			if (plane.find(key) != plane.end() ) { // if key exist
				ll y2 = plane[key];
				if (abs(y2-y)<L) {
					return false;
				}
			}
		}
	}
	return true;
}

int main() {
	// Unit tests:

	// ifstream in("in.txt");
	// streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	// cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	while	(cin >> N)	{
		plane.clear();
		for (ll i=0; i<N; ++i) {
			ll x,y;
			cin >> x >> y;
			plane[x] = y;
		}

		ll L=0, R=4000001, mid;
		while (R - L != 1) {
			mid = (L+R) >> 1;
			if (cover(mid)) {
				L = mid;
			} else {
				R = mid;
			}
		}

		cout << L << endl;
	}
	return 0;
}