'''
20.1
Write a function that adds two numbers. You should not use + or any arithmetic operators.
'''

'''
Can we make this a little easier? Yes! Imagine I decided to split apart the 'addition' and 'carry' steps. That is, I do the following:
1. Add 759 + 674, but 'forget' to carry. I then get 323.
2. Add 759 + 674 but only do the carrying, rather than the addition of each digit. I then get 1110.
3. Add the result of the first two operations (recursively, using the same process de- scribed in step 1 and 2): 1110 + 323 = 1433.
'''

def add(a,b):
    if b==0:
        return a
    c = a^b
    d = (a&b)<<1
    return add(c,d)
    

if __name__ == '__main__': 
    print add(10,19)
    
    
