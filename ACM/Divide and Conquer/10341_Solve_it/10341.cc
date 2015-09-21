#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>

using namespace std;

typedef long long ll;

ll p,q,r,s,t,u;

double f(double x) {
	return p*exp(-x)+q*sin(x)+r*cos(x)+s*tan(x)+t*x*x+u;
}

// negative return value means there is no solution;
double binary_solve(ll p, ll q, ll r, ll s, ll t, ll u) {
	double left=0, right=1;
	double y_l=f(left), y_r=f(right);
	if (y_l*y_r > 0) {
		return -1;
	}
	double mid = (left + right)/2, y_mid = f(mid);
	while (abs(y_mid) > 1.0e-10) {
		if (y_mid > 0) {
			left = mid;
		} else if (y_mid < 0) {
			right = mid;
		}
		mid = (left + right) / 2;
		y_mid = f(mid);
	}
	return mid;
}

int main() {
	// Unit tests:

	// ifstream in("in.txt");
	// streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	// cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	// ofstream out("out.txt");
	// streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	// cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	while(cin>>p>>q>>r>>s>>t>>u) {
		double val = binary_solve(p,q,r,s,t,u);
		if (val >= 0) {
			cout<<fixed<<setprecision(4) << val << endl;
		} else {
			cout << "No solution" << endl;
		}
	}
	return 0;
}