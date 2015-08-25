'''
8.4
Write a method to compute all permutations of a string.

if the method is given the string 'dog' as input, 
then it will print out the strings 'god', 'gdo', 'odg', 'ogd', 'dgo', and 'dog'
 - since these are all of the possible permutations of the string 'dog'. 
 Even if a string has characters repeated, each character should be treated
  as a distinct character - so if the string 'xxx' is input then your method 
  will just print out 'xxx' 6 times.
'''
# clarification quesitons:
# what does permutation mean? 
# what is the output? (a list of strings)
# can string by empty? (no)
# need an order? (no)           
    
import copy    
import math

def permutation(string):
    if len(string) == 1:
        return string
    
    output = []
    for i in range(len(string)):
        head = string[i]
        rest = string[:i]+string[i+1:]        
        output += [head+s for s in permutation(rest)]
    return output
    


if __name__ == '__main__':  
    print permutation('dog')
    print permutation('xxx')