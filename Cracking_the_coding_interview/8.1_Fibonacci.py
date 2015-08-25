'''
8.1 Write a method to generate the nth Fibonacci number.
'''


# clarification questions:
# 1) starts from 0 or 1? (0)

def Fib_recursive(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    return Fib_recursive(n-1)+Fib_recursive(n-2)
               
def Fib_dynamic(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    output = 1
    pre = 0
    while n > 2:
        new_pre = output
        output = pre + output
        pre = new_pre
        n -= 1
        
    return output
    
    

if __name__ == '__main__':
    for i in range(1,12):
        print Fib_recursive(i)
    print Fib_dynamic(500)