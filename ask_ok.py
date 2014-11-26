def ask_ok(prompt, retries=4,complaint='Yes or no, please!'):
    '''
    Created on Nov 22, 2014
    
    @author: Rick
    '''
    while True:
        ok = raw_input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n', 'no','nop','nope'):
            return False
        retries = retries-1
        if retries <0:
            raise IOError('refuseik user')
        print complaint
        
