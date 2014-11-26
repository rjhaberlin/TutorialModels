'''
Using lists as queues
(not recommended for efficiency because it is slowwww
Created on Nov 23, 2014

@author: Rick
'''
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print queue

