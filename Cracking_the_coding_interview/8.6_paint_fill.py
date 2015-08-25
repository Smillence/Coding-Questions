'''
8.6
Implement the 'paint fill' function that one might see on many image editing programs. That is, given a screen (represented by a 2 dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.

'''

# clarification quesitons:
# 1) the given point is white color? (not necessary, can be any color)
# 2) the fill color is not white? (not necessary)
# 3) what if the fill color is the same? (do nothing) 
# 4) input: a 2-D array; a pair of indecies representing a point; a new color
# 5) output: None. But the array might be changed
# 6) how do you define border? or how do you define whether two cells are connected? (connected only based on four direction-cells)

''' Algorithm design:
input: current cell position, arr, newcolor

if cell.color == newcolor: return
curcolor = cell.color
cell.color = newcolor
for each of the four directions:
    if that direction is out of bound of the arr: continue
    if color of the cell in that direction == curcolor:
        recursively call the function with the new cell as input
        

'''

# to simplify, assume color is just numbers
# 1 - white; 0 - black
def paintFill(arr,pos,color): 
    r = pos[0]
    c = pos[1]
    if arr[r][c] == color: return
    curcolor = arr[r][c]
    arr[r][c] = color
    newdirections = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
    r_MAX = len(arr) - 1
    c_MAX = len(arr[0]) - 1
    for new_r,new_c in newdirections:
        if 0<=new_r<=r_MAX and 0<=new_c<=c_MAX:
            if arr[new_r][new_c] == curcolor:
                paintFill(arr,(new_r,new_c),color)

                
                

if __name__ == '__main__':  
    
    arr = [
        [1,1,1,0,1,1,1],
        [1,1,1,0,1,1,1],
        [1,1,0,1,1,1,1],             
        [0,0,1,1,1,0,0],
        [1,1,1,1,0,1,1],
        [1,1,1,0,1,1,1],
        [1,1,1,0,1,1,1]
    ]
    
    pos = (3,3)
    color = 0
    
    paintFill(arr,pos,color)
    
    for r in arr:
        print r
    '''
    arr = [
        [1,1,1,0,0,0,0],
        [1,1,1,0,0,0,0],
        [1,1,0,0,0,0,0],             
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,1,1],
        [0,0,0,0,1,1,1],
        [0,0,0,0,1,1,1]     
    ]
    '''