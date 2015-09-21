#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;

char type;
ll row, col, counter;
vvi arr(200, vi(200));

void newline_helper() {
	if (counter == 50) {// maximum 50 chars per line
		cout << endl;
		counter = 1;
	} else {
		++counter;
	}
}

void B_2_D(ll row_min, ll row_max, ll col_min, ll col_max) {
	ll ele = arr[row_min][col_min];
	if (row_min == row_max && col_min == col_max) {
		newline_helper();
		cout << ele;
		return;
	}
	for (ll i=row_min; i<=row_max; ++i) {
		for (ll j=col_min; j<=col_max; ++j) {
			if (arr[i][j] != ele) {
				newline_helper();
				cout << "D";
				ll row_mid = (row_min+row_max) >> 1;
				ll col_mid = (col_min+col_max) >> 1;
				B_2_D(row_min, row_mid, col_min, col_mid); // top left
				if (col_mid+1 <= col_max)
					B_2_D(row_min, row_mid, col_mid+1, col_max); // top right
				if (row_mid+1 <= row_max)
					B_2_D(row_mid+1, row_max, col_min, col_mid); // bottom left
				if (row_mid+1 <= row_max && col_mid+1 <= col_max)
					B_2_D(row_mid+1, row_max, col_mid+1, col_max); // bottom right
				return;
			}
		}
	}
	newline_helper();
	cout << ele;
}

void D_2_B(ll row_min, ll row_max, ll col_min, ll col_max) {
	char c;
	cin>>c;
	if (c == '0') {
		for (ll i=row_min; i<=row_max; ++i)
			for (ll j=col_min; j<=col_max; ++j) 
				arr[i][j] = 0;
	} else if (c == '1') {
		for (ll i=row_min; i<=row_max; ++i)
			for (ll j=col_min; j<=col_max; ++j) 
				arr[i][j] = 1;
	} else {
		ll row_mid = (row_min+row_max) >> 1;
		ll col_mid = (col_min+col_max) >> 1;
		D_2_B(row_min, row_mid, col_min, col_mid); // top left
		if (col_mid+1 <= col_max)
			D_2_B(row_min, row_mid, col_mid+1, col_max); // top right
		if (row_mid+1 <= row_max)
			D_2_B(row_mid+1, row_max, col_min, col_mid); // bottom left
		if (row_mid+1 <= row_max && col_mid+1 <= col_max)
			D_2_B(row_mid+1, row_max, col_mid+1, col_max); // bottom right
	}
}

int main() {
	// Unit tests:

	// ifstream in("in.txt");
	// streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	// cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	// ofstream out("out.txt");
	// streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	// cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	while(cin>>type>>row>>col) {
		counter = 0;
		if (type == '#') {
			break;
		} 
		else if (type == 'B') {
			cout << 'D' << right << setw(4) << row << right << setw(4) << col << endl;
			char c;
			for (ll i=0; i<row; ++i) {
				for (ll j=0; j<col; ++j) {
					cin>>c;
					arr[i][j] = c - '0';
				}
			}
			B_2_D(0, row-1, 0, col-1);
		}
		else if (type == 'D') {
			cout << 'B' << right << setw(4) << row << right << setw(4) << col << endl;
			D_2_B(0, row-1, 0, col-1);
			for (ll i=0; i<row; ++i)
				for (ll j=0; j<col; ++j) {
					newline_helper();
					cout << arr[i][j];
				}
		}
		cout << endl;
	}
	return 0;
}