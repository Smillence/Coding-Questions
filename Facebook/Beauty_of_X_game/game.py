'''
The beauty of a number X is the number of 1s in the binary representation of X.

Two players are plaing a game. There is number n written on a black board. The game is played as following:

Each time a player chooses an integer number (0 <= k) so that 2^k is less than n and (n-2^k) has as beautiful as n.
Next he removes n from blackboard and writes n-2^k instead.

The player that can not continue the game (there is no such k that satisfies the constrains) looses the game.

The First player starts the game and they play in turns alternatively. Knowing that both two players play optimally you have to specify the winner.

Input:

First line of the Input contains an integer T, the number of testcase. 0 <= T <= 5.

Then follow T lines, each containing an integer n.

n more than 0 and less than 10^9 +1.

Output

For each testcase print "First Player" if first player can win the game and "Second Player" otherwise.

Sample Input

7
1
2
8
16
42
1000
123

Sample Output

Second Player
First Player
First Player
Second Player
Second Player
First Player
Second Player

Explanation

In the first example n is 1 and first player can't change it so the winner is the second player.

In the second example n is 2, so the first player subtracts 1 (2^0) from n and the second player looses the game.
'''

import sys
import string
digs = string.digits + string.letters

def int2base(x, base):
 
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)
    
# This function is not used
# x is positive
def beauty(x):
    string = int2base(x,2)    
    return len(filter(lambda x:x=='1',string))

# input number x=42,win=False
# process: 42->'101010' -> 11010 -> 10110 -> 1110-> 1101->1011->'111' -> 7
# output number x=7,win=False
def refactor(x,win):
    base=2
    string = int2base(x, base)
    try:
        k = len(string) - 1 - string.index('0')
        x = x - base**k
        return refactor(x,not win)
    except:
        return x,win

if __name__ == '__main__':
    '''
    for i in range(100):
        if beauty(i) != 2:continue
        string = int2base(i,2)
        print i,':',string,beauty(i)'''

    try:
        txt = open(sys.argv[1],"rt")
    except:
        print "File does not exist!"
        sys.exit()


    '''
    any given number say, 101010, can be reduced to form 11...1 and end of game
    base case is 1

    the quickest way for 101010 is -> 11010 -> 10110 -> 1110-> 1101->1011->111 (lose)

    the strategy is to scan the number from left to right and as soon as found a '0',
    reduce '1' at that position

    '''
    T= int(txt.readline())#number of test cases

    for t in range(T):

        x= int(txt.readline())

        x,win=refactor(x,False)

        if win:
            print 'First Player'
        else:
            print 'Second Player'

        
    