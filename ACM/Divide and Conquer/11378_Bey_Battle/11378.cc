#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

typedef long long ll;
// typedef vector<ll> vi;
// typedef vector<vi> vvi;
typedef map<ll, ll> dict;

ll N;
//vvi plane(100000, vi(2));
dict plane;

// bool compare(vi p1, vi p2) {
// 	return p1[0]<p1[0];
// }

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

	// ofstream out("out.txt");
	// streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	// cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	while	(cin >> N)	{
		plane.clear();
		for (ll i=0; i<N; ++i) {
			ll x,y;
			cin >> x >> y;
			plane[x] = y;
		}
		//sort(plane.begin(), plane.begin()+N, compare);

		ll L=0, R=4000001, mid;
		while (R - L != 1) {
			mid = (L+R) >> 1;
			//cout << R << " " << L<< " "  << mid << endl;
			if (cover(mid)) {
				L = mid;
			} else {
				R = mid;
			}
		}
		// for (ll i=0; i<N; ++i) {
		// 	// ll tmp = max(abs(plane[i][0] - plane[i+1][0]), abs(plane[i][1] - 
		// 	// 	plane[i+1][1]));
		// 	// Max = min(tmp, Max);
		// }
		cout << L << endl;
	}
	return 0;
}