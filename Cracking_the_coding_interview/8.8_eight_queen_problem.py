'''
8.8
Write an algorithm to print all ways of arranging eight queens on a chess board so that none of them share the same row, column or diagonal.
'''

# clarification quesitons:
# 1) what's the size of a chess board (8*8)
# 2) no order of the queens? (no)



import copy

# this function can solve n-queen problem
# return a list of list of tuples
# if no solution, return []
def eight_queen(grids,n): 
    if not grids:
        return []
        
    if n==1:
        return [[grid] for grid in grids]
        
    output = []
    cpy = copy.deepcopy(grids)
    for grid in grids:   
        cpy.remove(grid)
        newgrids = filter(lambda g:g[0]!=grid[0] and g[1]!=grid[1] and abs(g[1]-grid[1]) != abs(g[0]-grid[0]), cpy)
        subsolutions = eight_queen(newgrids,n-1)        
        if subsolutions:
            output += [path+[grid] for path in subsolutions]
        
    return output

                
                

if __name__ == '__main__':  
    
    arr = []
    for r in range(1,9):
        for c in range(1,9):
            arr.append((r,c))
    s = set(arr)
    for sol in eight_queen(s,8):
        print sol