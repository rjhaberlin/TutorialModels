def fib(n):
    ''' Print fibonacci up to n. The sum of two elements defines the next.
    Created on Nov 21, 2014
    
    @author: Rick
    '''
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b
        
fib(2000)

    

