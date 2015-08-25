import copy

# print in order?
# lst: ['a',['b',c',['d'],[['e']]]]
# precedor: 'String: '
def dumpList(precedor, lst):
    if not lst:
        return None

    lst = copy.deepcopy(lst)
    cur = lst.pop()
    
    dumpList(precedor,lst)
    
    if type(cur) is list:
        dumpList(precedor,cur)
    else:
        print precedor + cur
    
    

# test case demo: [[],'a']
# cur: 'a', lst: [[]]
# 'a'
# cur: [], lst: []
# 
    
if __name__ == '__main__':
    dumpList('Output: ',['a',['b','c',['d'],[['e']]]])
    dumpList('Output: ',[[],'a'])
