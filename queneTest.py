from collections import deque 
q=deque(range(5))
print(q)
q.append(5)
print(q)
q.appendleft(6)
print(q)
q.pop()
print(q)
q.rotate(2)
print(q)
