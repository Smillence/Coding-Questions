/*
m books with different pages
k scribers, k<m
each scriber get a continuous sequence of books

Goal: minimize the maximum number of pages assigned to a single scriber

*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

#include <cstring>


using namespace std;

typedef long long ll;
typedef vector<ll> vi;

vi pos;// the position of the slashes to divide the books to k parts
int use[510];

bool cover(ll range, ll k, vi* p) {
	pos.clear();
	ll cum = 0;
	for (ll i=(*p).size()-1; i>=0; --i) {
		if (cum + (*p)[i] > range) {
			pos.push_back(i+1); // slash after the book i+1
			cum = (*p)[i]; // reset
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

void print (ll high_bound, vi* p, ll m, ll k) {
	int group = 1, sum = 0;
	for (int i = m-1; i >= 0; i--) {
    if (sum + (*p)[i] > high_bound) {
    	use[i] = 1;
    	sum = (*p)[i];
    	group++;
    } else {
    	sum += (*p)[i];
    }
    if (k-group == i+1) {
    	for(int j = 0; j <= i; j++)
    		use[j] = 1;
    	break;
    }
  }
  for (int i = 0; i < m-1; i++) {
  	cout << (*p)[i] << " ";
  	if(use[i]) cout << "/ ";
  }
  cout << (*p)[m-1] << endl;
}

int main() {

	// Unit tests:

	// ifstream in("in.txt");
	// streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	// cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	// ofstream out("out.txt");
	// streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	// cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	ll N, m, k;
	cin >> N; // number of test cases;
	for (ll cs=0; cs<N; ++cs) {

		memset(use, 0, sizeof(use));

		cin >> m >> k;

		vi p(m); // store pages of each book
		ll low_bound = -1, high_bound = 0;
		for (ll i=0; i<m; ++i) {
			cin >> p[i];
			if (low_bound < p[i]) {
				low_bound = p[i];
			}
			high_bound += p[i];
		}

		// bi-greedy search to find the smallest range that fits
		while (low_bound != high_bound) {
			ll mid = (high_bound+low_bound) >> 1;
			if (cover(mid, k, &p)) {
				high_bound = mid;
			} else {
				low_bound = mid + 1;
			}
		}

		//print the result
		print(low_bound, &p, m, k);

	}
	return 0;
}
