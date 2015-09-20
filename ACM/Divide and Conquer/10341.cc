#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef double (*fptr) (double);

double Newton_Raphson(ll p, ll q, ll r, ll s, ll t, ll u) {
	double x = 0;
	double new_x = 1;
	while (abs(new_x-x) > 1.0e-6) {
		// f'(x)
		double a = -p*exp(-x)+q*cos(x)-r*sin(x)+s*(1+tan(x)*tan(x))+2*t*x;
		if (a == 0) {
			x += 0.1;
			continue;
		}
		// f(x)
		double y = p*exp(-x)+q*sin(x)+r*cos(x)+s*tan(x)+t*x*x+u;

		new_x = x - y/a;
		// x = y;
		// y = new_y;
		//cout << a << y << x << new_x << endl;
		//return 0;
		cout << a << " " <<new_x << endl;
		cout << x << " " <<new_x << endl;
	}
	return x;
}

// fptr equation_generator(ll p, ll q, ll r, ll s, ll t, ll u) {
// 	auto f = [](double x) { return 42; };  
// 	return f
// }

double foo(ll p, ll q, ll r, ll s, ll t, ll u) {
	double left=0, right=1;
	while (left - right > 1.0e-6) {
		double mid1 = 2*left/3 + right/3;
		double mid2 = 2*right/3 + left/3;
	}
	return 0;
}

int main() {
	auto f = []() { return 42; };
	ll p,q,r,s,t,u;
	for(ll cs = 0; cin>>p>>q>>r>>s>>t>>u ; ++cs) {
		cout << Newton_Raphson(p,q,r,s,t,u) << endl;
	}
	return 0;
}