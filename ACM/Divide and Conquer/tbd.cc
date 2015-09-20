/*
m books with different pages
k scribers, k<m
each scriber get a continuous sequence of books

Goal: minimize the maximum number of pages assigned to a single scriber

Teset cases:
1. k==1
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;

vi pos;// the position of the slashes to divide the books to k parts

bool cover(ll range, ll k, vi* p) {
	pos.clear();
	ll cum = 0;
	for (ll i=(*p).size()-1; i>=0; --i) {
		if ((*p)[i] > range) { // this will never happen, can be deleted
			return false;
		}
		if (cum > range) {
			pos.push_back(i+1); // slash after the book i+1
			cum = (*p)[++i]; // reset
		} else {
			cum += (*p)[i];
		}
	}
	if (cum > range) {
		pos.push_back(0); 
	}
	if (pos.size() <= k-1) {
		return true;
	} else {
		return false;
	}
}

int main() {
	ifstream in("in.txt");
  streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  ofstream out("out.txt");
  streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!


	ll N, m, k;
	cin >> N; // number of test cases;
	for (ll cs=0; cs<N; ++cs) {
		cin >> m >> k;

		vi p(m); // store pages of each book
		ll low_bound = -1, high_boud = 0;
		for (ll i=0; i<m; ++i) {
			cin >> p[i];
			if (low_bound < p[i]) {
				low_bound = p[i];
			}
			high_boud += p[i];
		}

		// vi p_cum(m); // cumulative
		// p_cum[0] = p[0];
		// for (ll i=1; i<m; ++i) {
		// 	p_cum[i] = p_cum[i-1] + p[i];
		// }

		// Step 1: bi-greedy search to find the smallest range that fits
		while (low_bound != high_boud) {
			ll mid = (high_boud+low_bound) / 2;
			if (cover(mid, k, &p)) {
				high_boud = mid;
			} else {
				low_bound = mid + 1;
			}
		}
		cover(low_bound, k, &p);
		//cout << "XXX" << low_bound <<" "<< high_boud<<"XXX";

		// while (cover(high_boud, k, &p)) {
		// 	high_boud /= 2;
		// }
		// while (!cover(high_boud, k, &p)) {
		// 	++high_boud;
		// }

		// Step 2: Satisfy that each scriber must be assigned at least one book
		reverse(pos.begin(),pos.end()); 
		ll rest = (k-1 - pos.size());
		ll start = 0;
		for (vi::iterator it=pos.begin(); it!=pos.end(); ++it) {
			for (ll i = start; rest > 0 && i<*it; i++, --rest) {
				pos.push_back(i);
			}
			if (rest == 0) {
				break;
			}
			start = *it + 1;
		}
		sort(pos.begin(), pos.end());

		// Step 3: print the result
		start = 0;
		for (vi::iterator it=pos.begin(); it!=pos.end(); ++it) {
			for (ll i = start; i<=*it; i++) {
				cout << p[i] << " ";
			}
			cout << "/ ";
			start = *it + 1;
		}
		for (ll i = start; i<m-1; ++i) {
			cout << p[i] << " ";
		}
		cout << p[m-1];
		cout << endl;
	}
	return 0;
}