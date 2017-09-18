'''
Question:
123456789 = 100 (also known as targetSum)
Using standard integer arithmeric operators +, -, how many different solutions
can you find by inserting the operators between some digits?

Solutions;
123-45-67+89 = 100
123-4-5-6-7+8-9 = 100
123+45-67+8-9 = 100
123+4-5+67-89 = 100
12-3-4+5-6+7+89 = 100
12+3-4+5+67+8+9 = 100
12+3+4+5-6-7+89 = 100
1+23-4+56+7+8+9 = 100
1+23-4+5+6+78-9 = 100
1+2+34-5+67-8+9 = 100
1+2+3-4+5+6+78+9 = 100
-1+2-3+4+5+6+78+9 = 100

'''

class Tree:
    def __init__(self, data: str) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.middle = None

class SolutionOne(object):
    def __init__(self, digits: str, target: int) -> None:
        self.digits = digits
        self.target = target

    def strToRes(self, s: str) -> int:
        """
        examples:
        '#-1#+2#-234#+6' -> -227
        '1#+2#-234#+6' -> -225
        """
        numbers = s.split('#')
        if numbers[0] == '':
            return sum([int(x) for x in numbers[1:]])
        else:
            return sum([int(x) for x in numbers])

    def evalAndPrint(self, s: str) -> None:
        if self.strToRes(s) == self.target:
            print(
                s.translate(str.maketrans('', '', '#')) + 
                ' = ' + 
                str(self.target)
            )

    def targetSum(self) -> None:
        root = Tree(None)
        self.createTree(root, 0, len(self.digits))
        self.tranverse(root, '', self.digits)

    def createTree(self, root: Tree, cur: int, depth: int) -> None:
        if cur == 0:
            root.left = Tree('')
            root.right = Tree('#-')
            self.createTree(root.left, cur+1, depth)
            self.createTree(root.right, cur+1, depth)
        elif cur < depth:
            root.left = Tree('')
            root.right = Tree('#-')
            root.middle = Tree('#+')
            self.createTree(root.left, cur+1, depth)
            self.createTree(root.right, cur+1, depth)
            self.createTree(root.middle, cur+1, depth)

    def tranverse(self, tree: Tree, cur_path: str, digits: str) -> None:
        if cur_path == '':
            self.tranverse(
                tree.left,
                cur_path + tree.left.data + digits[0],
                digits[1:],
            )
            self.tranverse(
                tree.right,
                cur_path + tree.right.data + digits[0],
                digits[1:],
            )
        elif tree.left == None and tree.middle == None and tree.right == None:
            self.evalAndPrint(cur_path)
        else:
            self.tranverse(
                tree.left,
                cur_path + tree.left.data + digits[0],
                digits[1:],
            )
            self.tranverse(
                tree.right,
                cur_path + tree.right.data + digits[0],
                digits[1:],
            )
            self.tranverse(
                tree.middle,
                cur_path + tree.middle.data + digits[0],
                digits[1:],
            )

class SolutionTwo(object):
    def __init__(self, digits: str, target: int) -> None:
        self.digits = digits
        self.target = target

    def evalAndPrint(self, s: str) -> None:
        if eval(s) == self.target:
            print(s + ' = ' + str(self.target))

    def targetSum(self) -> None:
        self.step('', 0)

    def step(self, path: str, i: int) -> None:
        if i >= len(self.digits):
            self.evalAndPrint(path)
            return

        self.step(path + '' + self.digits[i], i+1)
        self.step(path + '-' + self.digits[i], i+1)

        if i != 0:
            self.step(path + '+' + self.digits[i], i+1)

if __name__ == '__main__':
    print('=== solution 1 ===')
    SolutionOne('123456789', 100).targetSum()

    print('=== solution 2 ===')
    SolutionTwo('123456789', 100).targetSum()
