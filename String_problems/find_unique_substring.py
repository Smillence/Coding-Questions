'''
Facebook interview questions for intern:

You are given a set of unique characters and a string.

Find the smallest substring of the string containing all the characters in the set


Set : [a, b, c] 
String : "abbcbcba"
Ouput "cba"


 find all positions of 
[a,b,c]
'a': 0,7
'b': 1,2,4,6
'c': 3,5

for each combination (say 0,2,5), (max - min) (5-0=5) is the length of the substring

'''
import copy
# solution 1 - bruth-force
def foo_bruth_force(Set,String):
    positions = {char:[] for char in Set}
    for i in range(len(String)):
        if String[i] in positions:
            positions[String[i]].append(i)
    # positions {'a':[0,7],'b':[1,2,4,6],'c':[3,5],'d'....,'e',}
    
    positions = [positions[key] for key in positions]
    output = min(helper(positions), key=minmax )
    return String[output[0]:output[-1]+1]

# lst is a list of lists
# return a list of numbers
def helper(lst):
    lst = copy.deepcopy(lst)
    if len(lst)==0: return []
    
    sublst = lst.pop()# sublst [0,7]
    right = helper(lst) # a list of lists
    output = []
    for x in sublst:
        if len(lst)!=0:
            output += [ [x]+sub  for sub in right]
        else:
            output.append([x])
    return output


def minmax(lst):
    lst.sort()
    return lst[-1]-lst[0]
   
    
# not used; still in progress
# divide and concour
def foo(Set,String,index):
    set_length = len(Set)
    str_length = len(String)
    if str_length < set_length:
        return float('inf'),None
    elif str_length == set_length:
        if set(String) == set(Set):
            return set_length,index
        else:
            return float('inf'),None
    else:
        result_l = foo(Set,String[:str_length/2],index)
        result_r = foo(Set,String[str_length/2:],index+str_length/2)
        result = min(result_l,result_r,key=lambda x:x[0])
        k = result[0]
        print k,result_l,result_r
        middle = String[str_length/2 - k + 2:str_length/2 + k - 2]
        result_m = foo(Set,middle,index+str_length/2 - k + 2)
        result = min(result,result_m,key=lambda x:x[0])
        return result


if __name__ == '__main__':
    print foo_bruth_force(['a','b','c'],'abbcbcba')            
  
# a=['a', 'b', 'c']
# b=['a', 'c', 'b']
# a.sort()
# print set('abc') == set(['b', 'a', 'c','a'])
# print foo(['a', 'b', 'c'],'abbcbcba',0)
