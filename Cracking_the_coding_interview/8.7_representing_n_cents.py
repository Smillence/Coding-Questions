'''
8.7
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''
# n >0
def foo(n):        
    output = 0
    for i in range(1+n/25):
        for j in range(1+(n-25*i)/10):
            rest = n - 25*i - 10*j
            output += 1+rest / 5
            
    return output


if __name__ == '__main__':  
    print foo(25)