n = int(input())
m = int(input())

counter = 0
ops = []
for i in range(m):
    start, end = list(map(int, input().split()))
    counter += 1
    for k, j in enumerate(ops):
        if j:
            if (start >= j[0] and start <= j[1]) \
                or (end >= j[0] and end <= j[1]) \
                or (start <= j[0] and end >= j[1]):
                ops[k] = None
                counter -= 1
    ops.append((start, end))
print(counter)




