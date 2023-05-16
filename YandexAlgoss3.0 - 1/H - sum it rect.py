from array import array
from datetime import datetime

print(datetime.now())
f = open('input1.txt', 'r')

n, m, k = tuple(map(int, f.readline().strip().split()))


def prefix_sum(strg: str) -> array:
    lst = strg.strip().split()
    prefix_lst: list[int] = list()
    prefix_lst.append(int(lst[0]))
    for i in lst[1:]:
        prefix_lst.append(prefix_lst[-1] + int(i))
    return array('l', prefix_lst)


matrix = [prefix_sum(f.readline()) for _ in range(n)]


def sum_in_rect(lst: list[array], ask: tuple[int]) -> None:
    res = 0
    for i in range(ask[0]-1, ask[2]):
        res += lst[i][ask[3] - 1] - (0, lst[i][ask[1] - 2])[ask[1] >= 2]
    # return str(res) + '\n'
    print(res)


[(sum_in_rect(matrix, j)) for j in (tuple(map(int, f.readline().strip().split())) for _ in range(k))]
