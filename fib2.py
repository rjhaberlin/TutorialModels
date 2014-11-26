def fib2(n):
    '''
    Created on Nov 22, 2014
    
    @author: Rick
    '''
  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result