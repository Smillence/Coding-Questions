#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

const int MAXN = 510;

int a[MAXN], use[MAXN];
long long  low_bound, high_bound;
int n, m;

void init()
{
    low_bound = -1;
    high_bound = 0;
    memset(use, 0, sizeof(use));
}

int solve(int mid)
{
    int sum = 0, group = 1;
    for(int i = n-1; i >= 0; i--)
    {
        if(sum + a[i] > mid)
        {
            sum = a[i];
            group++;
            if(group > m) return 0;
        }
        else sum += a[i];
    }
    return 1;
}

void print(int high_bound)
{
    int group = 1, sum = 0;
    for(int i = n-1; i >= 0; i--)
    {
        if(sum + a[i] > high_bound)
        {
            use[i] = 1;
            sum = a[i];
            group++;
        }
        else sum += a[i];
        if(m-group == i+1)
        {
            for(int j = 0; j <= i; j++)
                use[j] = 1;
            break;
        }
    }
    for(int i = 0; i < n-1; i++)
    {
        cout << a[i] << " ";
        if(use[i]) cout << "/ ";
    }
    cout << a[n-1] << endl;
}

int main()
{
    ifstream in("in.txt");
  streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  ofstream out("out2.txt");
  streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!



    int T;
    cin >> T;
    while(T--)
    {
        init();
        cin >> n >> m;
        for(int i = 0; i < n; i++)
        {
            cin >> a[i];
            if(low_bound < a[i]) low_bound = a[i];
            high_bound += a[i];
        }
        long long x = low_bound, y = high_bound;
        while(x <= y)
        {
            long long  mid = x+(y-x)/2;
            if(solve(mid)) y = mid-1;
            else x = mid+1;
        }
        print(x);
    }
    return 0;
}
