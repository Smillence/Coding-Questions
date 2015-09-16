#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;

int main() {
	ll N, Q, height;
	cin >> N; // number of chimps
	vi chimps(N);
	for (ll i=0; i<N; ++i) {
		cin >> chimps[i]; // read in heights of lady chimps
	}
	cin >> Q; // number of queries
	for (ll i=0; cin >> height; ++i) { // height of the chimpanzee
		
		if (chimps[0] == height && chimps[N-1] == height) { // no fit
			cout << "X X" <<endl;
		} else if (chimps[0] > height) { // one fit
			cout << "X " << chimps[0] <<endl;
		} else if (chimps[N-1] < height) { // one fit
			cout << chimps[N-1] << " X" <<endl;
		} else { // two fit and one fit
			bool left_x = false;
			bool right_x = false;
			ll left=0;
			ll right=N-1;
			while (right - left > 1) {
				ll mid = (left+right) / 2;
				if (chimps[mid] < height) {
					left = mid;
				} else if (chimps[mid] > height) {
					right = mid;
				} else { // it will be tricky when find a tie
					// 1. find left
					left = mid;
					while (left-1 >= 0) {
						--left;
						if (chimps[left] < height) {
							break;
						}
					}
					if (chimps[left] >= height) {
						left_x = true;
					}

					// 2. find right
					right = mid;
					while (right+1 <= N-1) {
						++right;
						if (chimps[right] > height) {
							break;
						}
					}
					if (chimps[right] <= height) {
						right_x = true;
					}

					break;
				}
			}

			if (chimps[left] >= height) {
				left_x = true;
			}
			if (chimps[right] <= height) {
				right_x = true;
			}

			// print
			if (left_x) {
				cout << "X ";
			} else {
				cout << chimps[left] << " ";
			}
			if (right_x) {
				cout << "X" << endl;;
			} else {
				cout << chimps[right] << endl;
			}

		}
	}
	return 0;
}

/**
Test case 1:
1
1
3
0 1 2

Test case 2:
2
1 1
3
0 1 2

Test case 3:
2
1 2
4
0 1 2 3

Test case 4:
2
1 3
5
0 1 2 3 4

Test case 5:
3
1 1 1
3
0 1 2

Test case 6:
3
1 1 2
4
0 1 2 3

Test case 7:
3
1 1 3
5
0 1 2 3 4

Test case 8:
3
1 3 3
5
0 1 2 3 4

Test case 9:
3
1 2 2
4
0 1 2 3

Test case 10:
3
1 2 3
5
0 1 2 3 4

Test case 11:
3
1 2 4
6
0 1 2 3 4 5

Test case 12:
3
1 3 5
7
0 1 2 3 4 5 6

Test case 13:
6
1 2 4 6 6 6
8
0 1 2 3 4 5 6 7

Test case 14:
6
3 3 3 4 6 9
9
2 3 4 5 6 7 8 9 10
**/