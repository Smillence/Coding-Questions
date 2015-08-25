'''
8.5
Implement an algorithm to print all valid 
(e.g., properly opened and closed) combinations of n-pairs of parentheses.
'''

# number of left and right parenthesis not used yet
def valid_parenthesis(n):
    return foo(n,n)

def foo(L,R):
    if L==0:
        return [''.join([')' for i in range(R)])]
    
    if L == R:
        return ['('+s for s in foo(L-1,R)]
    else:
        first = ['('+s for s in foo(L-1,R)]
        second = [')'+s for s in foo(L,R-1)]
        return first + second
 


if __name__ == '__main__':  
    print valid_parenthesis(3)