n = int(input())

out = [None,None,None,None]

for i in range(n):
    k = list(map(int, input().split()))
    if out[0] is None:
        out[0] = out[2] = k[0]
        out[1] = out[3] = k[1]
    else:
        if k[0] < out[0]:
            out[0] = k[0]
        elif k[0] > out[2]:
            out[2] = k[0]
        if k[1] < out[1]:
            out[1] = k[1]
        elif k[1] > out[3]:
            out[3] = k[1]
print(*out)
