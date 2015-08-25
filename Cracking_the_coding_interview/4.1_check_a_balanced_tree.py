'''
4.1
Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.
'''

''' Sudo code: the idea is to use BFS

frontier = [root]

leaf_d = None

while frontier != []:
    cur = frontier.pop_from_the_beginning
    if cur has child:
        frontier.add_to_end(all children)
    else:
        if leaf_d == None:
            lead_d = cur.depth
        else:
            if cur.depth > lead_d+1:
                return not balanced
return balanced
            
'''
class Tree:
    def __init__(self):
        self.left = None
        self.right = None
    
        
    def isBalanced(self):
        frontier = [(self,0)]
        leaf_d = None
        while frontier != []:
            cur = frontier.pop(0)
            hasChild = False
            if cur[0].left != None:
                hasChild = True
                frontier.append((cur[0].left,1+cur[1]))
            if cur[0].right != None:
                hasChild = True
                frontier.append((cur[0].right,1+cur[1]))
            if not hasChild:
                if leaf_d == None:
                    leaf_d = cur[1]
                elif cur[1] > leaf_d + 1:
                    return False
        return True
                    

if __name__ == '__main__':
    a = Tree()
    b = Tree()
    c = Tree()
    d = Tree()
    e = Tree()
    a.left = b
    a.right = c
    b.left=d
    d.right=e
    print a.isBalanced()
    d.right = None
    c.right=e
    print a.isBalanced()

