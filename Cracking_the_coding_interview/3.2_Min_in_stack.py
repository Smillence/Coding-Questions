'''
3.2
How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.
'''

# add(item)
# pop()
# Min() - stack should not be empty; or will report error
# 3(3),2(2),1(1),5(1)

class MinStack:
    def __init__(self):
        self.stack = []
    def add(self,item):
        Min = None
        if self.stack == []:
            Min = item         
        else:
            Min = min(self.stack[-1][1],item)
        self.stack += [(item,Min)]
    def pop(self):
        pair = self.stack.pop()
        return pair[0]
    def Min(self):
        return self.stack[-1][1]
        

    
    

if __name__ == '__main__':
    a = MinStack()
    a.add(3)
    a.add(1)
    a.add(2)
    a.add(5)
    a.add(0)
    print a.Min()
    print a.pop(),a.Min(),a.stack
    print a.pop(),a.Min(),a.stack
    print a.pop(),a.Min(),a.stack
    print a.pop(),a.Min(),a.stack
    print a.pop(),a.stack

