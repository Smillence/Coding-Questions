'''
9.6
Given a matrix in which each row and each column is sorted, write a method to find an element in it.
'''

# clarification quesitons:
# can there be duplicates? (yes)
# the matrix size is at least 1*1? (yes)
# what if cannot found (return None)
    
# modified binary search in 2-dimension
# compare with mid=(row/2,col/2)
# if x < mid: bottom-right corner is eliminated;
# else: up-left corner is eliminated
# after elimination, run the algorithm recursively
# each round can shrink 1/4 size
# so the run-time complexity is O(log{4/3}{row*col})

# m is 2-D array
def searchMatrix(m,row,col,x,origin):
    r,c = origin
    
    if row*col==0:
        return None
    
    mid = m[r+row/2][c+col/2]
    if x==mid: 
        return r+row/2,c+col/2
    elif x<mid:
        result = None
        result = searchMatrix(m,row,col/2,x,origin)
            
        if result != None:
            return result
        else:
            return searchMatrix(m,row/2,col-col/2,x,(r,c+col/2))
    else:
        result = None
        result = searchMatrix(m,row,col-col/2-1,x,(r,c+col/2+1))
            
        if result != None:
            return result
        else:
            return searchMatrix(m,row-row/2-1,col/2+1,x,(r+row/2+1,c))
        
    
    
if __name__ == '__main__': 
    m = [
        [1,2,6,7,11],
        [3,5,9,13,16],
        [4,10,14,18,22],
        [8,12,17,21,23],
        [15,19,20,24,25]
    ]
    for x in range(1,27):
        print searchMatrix(m,5,5,x,(0,0))