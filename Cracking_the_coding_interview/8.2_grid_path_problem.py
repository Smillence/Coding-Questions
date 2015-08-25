'''
8.2
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are 'off limits', such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.

'''
from math import factorial
# solution 1: recursion
def searchGrid(m,n):
    if m > 0 and n > 0:
        return searchGrid(m-1,n) + searchGrid(m,n-1)
    else:
        return 1

    
def searchGrid_2(m,n):
    # choose m from (m+n)
    return factorial(m+n) / (factorial(m)*factorial(n))

def robotSearch(N):
    return searchGrid_2(N-1,N-1)

# a list of wall locations
# walls = [(1,1)]
def robotSearch_followUp(N,walls):
    return searchGrid_followUp(N-1,N-1,walls)
    
def searchGrid_followUp(m,n,walls):
    if (m,n) in walls:
        return 0
    if m > 0 and n > 0:   
        return searchGrid_followUp(m-1,n,walls) + searchGrid_followUp(m,n-1,walls)
    elif m > 0:
        return searchGrid_followUp(m-1,n,walls)
    elif n > 0:
        return searchGrid_followUp(m,n-1,walls)
    else:
        return 1
    
if __name__ == '__main__':
    print searchGrid(0,0)
    print searchGrid(3,3)
    print searchGrid_2(4,4)
    print robotSearch(3)
    print robotSearch_followUp(3,[(0,0)])
    print robotSearch_followUp(3,[(1,1)])
    print robotSearch_followUp(3,[(1,1),(0,2)])
    
        
    