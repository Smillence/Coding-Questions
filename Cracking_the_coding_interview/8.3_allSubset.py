'''
8.3
Write a method that returns all subsets of a set
'''
#clarification questions:
# 1) input: a set: s = set([5,2,4,7,8])
# 2) output: a list of sets
# 3) empth set will just return empth set?

import copy

def allSubset(s):
    if not s:
        return [s]
    cur = s.pop()
    output = allSubset(s)
    cpy_output = copy.deepcopy(output)
    for e in cpy_output:
        e.add(cur)
    output += cpy_output
    return output
    
    
if __name__ == '__main__':
    print allSubset(set([5,2,8]))
    print allSubset(set([7]))

    
        
    