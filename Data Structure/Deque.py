
from collections import deque 

L = [1,2,3,4,5]

q = deque(L)

print(q)

q.append(6)

print(q)

q.appendleft(7)

print(q)

q.pop()

print(q)

q.popleft()

print(q)

q.extend([10,20,30])

print(q)

q.extendleft([11,22,33,44])

print(q) 

q.rotate(2)

print(q)