from collections import deque

lst1 = [int(i) for i in input().split()]
lst2 = deque([int(i) for i in input().split()])
res = []
for i in lst1:
    while lst2 and lst2[0] < i:
        res.append(lst2.popleft())
    res.append(i)
res.extend(lst2)
print(*res)