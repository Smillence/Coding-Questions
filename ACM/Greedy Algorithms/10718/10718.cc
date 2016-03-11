/*
Algorithm design:

first we locate the valid bits of the number N. For example, for 100 50 60,
the valid bits are the last four bits. Becasue we have:

100 - 1100100
50 -   110010
60 -   111100

We can notice that 50 and 60 has the first bits in common.

Let's substract 32 from them.
50-32-16 = 2  - 0010
60-32-16 = 12 - 1100

So we only need to focus on the last four digits of 100, which is:
0100

So the best possible four bits are:
1011

Now we scan from the leftmost (greediest),

can we have 1?
- 1000 is in range [0010, 1100]. yes
can we have 0?
- 1000 is in range [0010, 1100]. yes
can we have 1?
- 1010 is in range [0010, 1100]. yes
can we have 1?
- 1011 is in range [0010, 1100]. yes

Now let's change to another situation. What if the range is [0010, 1000]

can we have 1?
- 1000 is in range [0010, 1000]. yes
can we have 0?
- 1000 is in range [0010, 1000]. yes
can we have 1?
- 1010 is not in range [0010, 1000]. no
So the solution is 1010 plue the first two bits. the number is 111010 = 58
*/

#include <iostream>
#include <fstream>

using namespace std;

typedef long long ll;

int main() {
	
}