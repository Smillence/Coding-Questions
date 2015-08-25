'''
# there are n versions on git
# goal: find out which version is bad? 
'''


# good v1 <- input1 (good revision)
# commits
# bad v2
#commits
# revision v3 <- input2 (revision at which repo is bad)
#commits

# v1,....vk are good
# vk+1 is bad
# --> vk+2,vk+3,....vn ALL BAD

#helper funciton already given
# e.g.
#checker(1) -> True
#checker(2) -> False
def checker(version):
    if version >=4:
        return False
    else:
        return True

# Design solutoin:
# 1) bruth-force (scan from beginning)
# 2) binary-search O(logn)

# if there does not exist bad commit, return -1
# else return the first bad commit number
def findTheBadCommit(v1,v2):
    if v1 == v2:
        if checker(v1):
            return -1 # all good
        else:
            return v1


    if v2 - v1 == 1:
        if not checker(v1):
            return v1
        elif not checker(v2):
            return v2
        else:
            return -1 # all good
    
    mid = (v1+v2)/2
    if checker(mid):
        # search right
        return findTheBadCommit(mid,v2) # 5,6
    else:
        # search left
        return findTheBadCommit(v1,mid) # 2,3,4 (4 is bad)

if __name__ == '__main__':
    print findTheBadCommit(2,5)
    
    