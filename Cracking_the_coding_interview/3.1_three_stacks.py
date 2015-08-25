'''
3.1
Describe how you could use a single array to implement three stacks.
'''

# add(i,item)
# pop(i)
# Note: i can be 0,1,2
class ThreeStacks:
    def __init__(self):
        self.stacks = []
    def add(self,i,item):
        self.stacks += [i,item]
    def pop(self,index):
        for i in range(len(self.stacks)-2,-1,-2):
            if self.stacks[i] == index:
                output = self.stacks[i+1]
                self.stacks[i:i+2] = []
                return output
        

    
    

if __name__ == '__main__':
    a = ThreeStacks()
    a.add(0,1)
    a.add(0,2)
    a.add(1,3)
    a.add(2,4)
    a.add(1,5)
    print a.pop(0),a.stacks
    print a.add(2,6),a.stacks
    print a.pop(0),a.stacks
    print a.pop(1),a.stacks
    print a.pop(1),a.stacks
    print a.pop(2),a.stacks
    print a.pop(2),a.stacks
    print a.pop(2),a.stacks
