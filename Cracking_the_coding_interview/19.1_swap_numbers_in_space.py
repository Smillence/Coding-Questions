'''
19.1
Write a function to swap two numbers in place without temporary variables.

'''
def foo(a,b):
    a +=b
    b = a-b
    a -= b
    return a,b

    
def foo2(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
    
if __name__ == '__main__': 
    print foo(10,19)
    print foo2(10,19)