'''
9.1 You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
'''
import copy


# clarification questions:
# 1) increasing order? (yes)
# 2) when there is a tie, a goes first? (yes)

# solution:
# merge from the tail but not the head
def merge(a,b):
    b = copy.deepcopy(b)
    pt_a = len(a)-1
    pt_b = len(b)-1
    cur = pt_a + pt_b + 1
    [a.append(None) for i in b]
    while pt_a >=0 and pt_b >=0:
        if a[pt_a] <= b[pt_b]:
            a[cur] = b[pt_b]
            cur -= 1
            pt_b -= 1
        else:
            a[cur] = a[pt_a]
            cur -= 1
            pt_a -= 1
    if pt_a < 0:
        a[:cur] = b[:pt_b]
    

if __name__ == '__main__':
    a = [1,3,5,7,9]
    b = [2,4,6,8]
    merge(a,b)
    print a
